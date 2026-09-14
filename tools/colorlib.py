"""Color engine for the Omarchy accessible theme set.

Pure stdlib. Implements:
  - sRGB <-> linear <-> Oklab/Oklch
  - WCAG 2.x relative-luminance contrast
  - APCA (SAPC-98 / W3C draft constants) lightness contrast Lc
  - Machado et al. (2009) CVD simulation matrices (severity 1.0)
  - Binary search for the Oklch lightness that hits a target WCAG contrast
"""
import math

# ---------- sRGB <-> linear ----------

def _s2l(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def _l2s(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * (c ** (1 / 2.4)) - 0.055

def hex_to_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#" + "".join(f"{max(0, min(255, round(c * 255))):02X}" for c in rgb)

def linear(rgb):
    return tuple(_s2l(c) for c in rgb)

def unlinear(lin):
    return tuple(_l2s(c) for c in lin)

# ---------- Oklab / Oklch ----------

def linear_to_oklab(lin):
    r, g, b = lin
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(v) ** (1 / 3), v) for v in (l, m, s))
    return (
        0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_,
        1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_,
        0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_,
    )

def oklab_to_linear(lab):
    L, a, b = lab
    l_ = L + 0.3963377774 * a + 0.2158037573 * b
    m_ = L - 0.1055613458 * a - 0.0638541728 * b
    s_ = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = (v ** 3 for v in (l_, m_, s_))
    return (
        +4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s,
    )

def oklch_to_linear(L, C, H):
    h = math.radians(H)
    return oklab_to_linear((L, C * math.cos(h), C * math.sin(h)))

def in_gamut(lin, eps=1e-4):
    return all(-eps <= c <= 1 + eps for c in lin)

def oklch_to_hex(L, C, H):
    """Convert with chroma reduction until the colour fits sRGB."""
    lo, hi = 0.0, C
    if in_gamut(oklch_to_linear(L, C, H)):
        best = C
    else:
        for _ in range(40):
            mid = (lo + hi) / 2
            if in_gamut(oklch_to_linear(L, mid, H)):
                lo = mid
            else:
                hi = mid
        best = lo
    lin = oklch_to_linear(L, best, H)
    return rgb_to_hex(tuple(max(0.0, min(1.0, c)) for c in unlinear(lin)))

def hex_to_oklch(h):
    L, a, b = linear_to_oklab(linear(hex_to_rgb(h)))
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360

# ---------- WCAG 2.x ----------

def rel_luminance(h):
    r, g, b = linear(hex_to_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b

def contrast(a, b):
    la, lb = rel_luminance(a), rel_luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

# ---------- APCA (W3C draft constants, 0.1.9) ----------

_APCA = dict(
    Ntx=0.57, Nbg=0.56, Rtx=0.62, Rbg=0.65,
    Bclip=1.414, Bthrsh=0.022, Wscale=1.14, Woffset=0.027, Wclamp=0.1,
)

def _apca_y(h):
    r, g, b = hex_to_rgb(h)
    f = lambda c: c ** 2.4
    return 0.2126729 * f(r) + 0.7151522 * f(g) + 0.0721750 * f(b)

def apca_lc(text, bg):
    """Signed Lc. Negative = light text on dark background."""
    P = _APCA
    ytx, ybg = _apca_y(text), _apca_y(bg)
    soft = lambda y: y if y > P["Bthrsh"] else y + (P["Bthrsh"] - y) ** P["Bclip"]
    ytx, ybg = soft(ytx), soft(ybg)
    if abs(ybg - ytx) < 0.0005:
        return 0.0
    if ybg > ytx:  # normal polarity: dark text on light bg
        S = (ybg ** P["Nbg"] - ytx ** P["Ntx"]) * P["Wscale"]
        out = 0.0 if S < P["Wclamp"] else S - P["Woffset"]
    else:          # reverse polarity: light text on dark bg
        S = (ybg ** P["Rbg"] - ytx ** P["Rtx"]) * P["Wscale"]
        out = 0.0 if S > -P["Wclamp"] else S + P["Woffset"]
    return round(out * 100, 1)

# ---------- CVD simulation: Machado, Oliveira & Fernandes (2009), severity 1.0 ----------

_CVD = {
    "protan": ((0.152286, 1.052583, -0.204868),
               (0.114503, 0.786281, 0.099216),
               (-0.003882, -0.048116, 1.051998)),
    "deutan": ((0.367322, 0.860646, -0.227968),
               (0.280085, 0.672501, 0.047413),
               (-0.011820, 0.042940, 0.968881)),
    "tritan": ((1.255528, -0.076749, -0.178779),
               (-0.078411, 0.930809, 0.147602),
               (0.004733, 0.691367, 0.303900)),
}

def simulate(h, kind):
    m = _CVD[kind]
    lin = linear(hex_to_rgb(h))
    out = tuple(sum(m[i][j] * lin[j] for j in range(3)) for i in range(3))
    out = tuple(max(0.0, min(1.0, c)) for c in out)
    return rgb_to_hex(unlinear(out))

def oklab_distance(a, b):
    la = linear_to_oklab(linear(hex_to_rgb(a)))
    lb = linear_to_oklab(linear(hex_to_rgb(b)))
    # weight lightness normally; Oklab is already roughly perceptually uniform
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(la, lb)))

# ---------- solver ----------

def solve_for_contrast(hue, chroma, bg, target, darker):
    """Find the Oklch lightness whose colour hits `target` WCAG contrast vs bg.

    darker=True searches below the background lightness (light themes),
    darker=False searches above it (dark themes).
    """
    lo, hi = (0.02, 0.99)
    for _ in range(60):
        mid = (lo + hi) / 2
        c = contrast(oklch_to_hex(mid, chroma, hue), bg)
        if darker:
            # lower L -> higher contrast
            if c > target:
                lo = mid
            else:
                hi = mid
        else:
            if c > target:
                hi = mid
            else:
                lo = mid
    L = lo if darker else hi
    return oklch_to_hex(L, chroma, hue)
