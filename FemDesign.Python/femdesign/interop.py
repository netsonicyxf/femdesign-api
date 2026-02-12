from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "urn:strusoft"


class EcG2SeismicGroundType(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"


@dataclass(kw_only=True)
class EcG2SpectraRecordType:
    class Meta:
        name = "EC_G2_spectra_record_type"

    t: float = field(
        metadata={
            "name": "T",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 12.0,
        }
    )
    sr: float = field(
        metadata={
            "name": "Sr",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 20.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EcG2VerticalSpectraType:
    class Meta:
        name = "EC_G2_vertical_spectra_type"

    beta_v: float = field(
        metadata={
            "name": "BetaV",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class AllLevelsType:
    class Meta:
        name = "all_levels_type"

    strata_top_levels: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_inclusive": -1000000.0,
            "max_inclusive": 10000.0,
            "tokens": True,
        },
    )
    water_levels: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_inclusive": -100000.0,
            "max_inclusive": 10000.0,
            "tokens": True,
        },
    )


class AngleunitType(Enum):
    DEGREE = "degree"
    RAD = "rad"


class ArrowtypeType(Enum):
    OPEN = "open"
    CLOSE = "close"
    BREAK = "break"
    FILL = "fill"
    CIRCLE = "circle"
    DOT = "dot"
    TICK = "tick"


class AutoForceSignType(Enum):
    PLUS = "plus"
    MINUS = "minus"


class AutoForceTypeType(Enum):
    SNOW = "snow"
    WIND = "wind"
    DEVIATION = "deviation"
    NOTIONAL = "notional"


class AxisPosition(Enum):
    START = "start"
    END = "end"
    BOTH = "both"


class BarBucklingType(Enum):
    FLEXURAL_WEAK = "flexural_weak"
    FLEXURAL_STIFF = "flexural_stiff"
    PRESSURED_FLANGE = "pressured_flange"
    LATERAL_TORSIONAL = "lateral_torsional"
    PRESSURED_BOTTOM_FLANGE = "pressured_bottom_flange"


@dataclass(kw_only=True)
class BarStiffnessFactorRecord:
    class Meta:
        name = "bar_stiffness_factor_record"

    cross_sectional_area: float = field(
        metadata={
            "name": "cross-sectional_area",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        }
    )
    shear_area_direction_1: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        },
    )
    shear_area_direction_2: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        },
    )
    torsional_constant: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        },
    )
    inertia_about_axis_1: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        },
    )
    inertia_about_axis_2: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BeamEdType:
    class Meta:
        name = "beam_ed_type"

    t_left: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    t_right: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class BeamposType(Enum):
    CENTER_OF_GRAVITY = "center_of_gravity"
    SHEAR_CENTER = "shear_center"
    BOUNDING_RECTANGLE = "bounding_rectangle"


class Beamtype(Enum):
    BEAM = "beam"
    COLUMN = "column"
    TRUSS = "truss"


@dataclass(kw_only=True)
class BoltLengthType:
    class Meta:
        name = "bolt_length_type"

    l: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 500.0,
        }
    )
    ls: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 500.0,
        }
    )
    lg: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 500.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BridgePierType:
    class Meta:
        name = "bridge_pier_type"

    elements: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            "tokens": True,
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,40}",
        }
    )
    colour: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Fa-f]{6}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BsType:
    class Meta:
        name = "bs_type"

    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CamberType:
    class Meta:
        name = "camber_type"

    force: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10000000000.0,
        }
    )
    e: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CamberType2D:
    class Meta:
        name = "camber_type_2d"

    force: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10000000000.0,
        }
    )
    e_y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -10000.0,
            "max_inclusive": 10000.0,
        }
    )
    e_z: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -10000.0,
            "max_inclusive": 10000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class CcType(Enum):
    CRISFIELD = "Crisfield"
    CERVERA = "Cervera"
    HINTON = "Hinton"
    PRAGER = "Prager"


class CementType(Enum):
    VALUE = ""
    CLASS_N = "Class N"
    CLASS_R = "Class R"
    CLASS_S = "Class S"


@dataclass(kw_only=True)
class CltLayer:
    class Meta:
        name = "clt_layer"

    material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,256}",
        }
    )
    thickness: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    theta: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.5707963267949,
        }
    )
    ex: float = field(
        metadata={
            "name": "Ex",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    ey: float = field(
        metadata={
            "name": "Ey",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    nuxy: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    gxy: float = field(
        metadata={
            "name": "Gxy",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    gxz: float = field(
        metadata={
            "name": "Gxz",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    gyz: float = field(
        metadata={
            "name": "Gyz",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    rho: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    fm0k: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    fm90k: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    ft0k: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    ft90k: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    fc0k: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    fc90k: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    fxyk: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    fvk: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    f_rk: float = field(
        metadata={
            "name": "fRk",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    f_tork: float = field(
        metadata={
            "name": "fTork",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CompositePartType:
    class Meta:
        name = "composite_part_type"

    material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    section: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    cog_offset_x: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        },
    )
    cog_offset_y: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class CompositePropName(Enum):
    B = "b"
    B_EFF = "b_eff"
    BB = "bb"
    BC = "bc"
    BF = "bf"
    BT = "bt"
    CY = "cy"
    CZ = "cz"
    D = "d"
    D1 = "d1"
    D2 = "d2"
    FILL_BEAM = "fill_beam"
    H = "h"
    HC = "hc"
    NAME = "name"
    O1 = "o1"
    O2 = "o2"
    T = "t"
    TF = "tf"
    TFB = "tfb"
    TFT = "tft"
    TH = "th"
    TW = "tw"


@dataclass(kw_only=True)
class CompositeSectionType:
    class Meta:
        name = "composite_section_type"

    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    pos: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class CompositeType(Enum):
    BEAM_A = "beam_a"
    BEAM_B = "beam_b"
    BEAM_P = "beam_p"
    COLUMN_A = "column_a"
    COLUMN_C = "column_c"
    COLUMN_D = "column_d"
    COLUMN_E = "column_e"
    COLUMN_F = "column_f"
    COLUMN_G = "column_g"


@dataclass(kw_only=True)
class ConnectivityType:
    class Meta:
        name = "connectivity_type"

    predefined_connectivity: str = field(
        default="00000000-0000-0000-0000-000000000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    m_x: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    m_x_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    m_y: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    m_y_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    m_z: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    m_z_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    r_x: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    r_x_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    r_y: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    r_y_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    r_z: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    r_z_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    v_x: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    v_x_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class CsPartType(Enum):
    ONLY_IN_THIS_STAGE = "only_in_this_stage"
    FROM_THIS_STAGE_ON = "from_this_stage_on"
    SHIFTED_FROM_FIRST_STAGE = "shifted_from_first_stage"
    ONLY_STAGE_ACTIVATED_ELEM = "only_stage_activated_elem"


class DetachType(Enum):
    VALUE = ""
    X_TENS = "x_tens"
    X_COMP = "x_comp"
    Y_TENS = "y_tens"
    Y_COMP = "y_comp"
    Z_TENS = "z_tens"
    Z_COMP = "z_comp"


@dataclass(kw_only=True)
class DimXType:
    class Meta:
        name = "dim_x_type"

    x: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DimYType:
    class Meta:
        name = "dim_y_type"

    y: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DimdimlineType:
    class Meta:
        name = "dimdimline_type"

    extension_a: float = field(
        default=0.005,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e23,
        },
    )
    penwidth: float = field(
        default=0.00018,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e23,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class Direction2DType(Enum):
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"


class DirectionType(Enum):
    X = "x"
    Y = "y"


class Displaymodes(Enum):
    WIREFRAME = "wireframe"
    HIDDEN_LINE = "hidden_line"
    SHADE = "shade"
    SHADE_WITH_EDGES = "shade_with_edges"


class Ec40TcType(Enum):
    VALUE_0_7 = 0.7
    VALUE_1_0 = 1.0
    VALUE_1_6 = 1.6


class Edgetype2(Enum):
    LINE = "line"
    ARC = "arc"
    SPLINE = "spline"
    POLYLINE = "polyline"
    CIRCLE = "circle"


@dataclass(kw_only=True)
class EmptyType:
    class Meta:
        name = "empty_type"


@dataclass(kw_only=True)
class EntityColor:
    class Meta:
        name = "entity_color"

    tone: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Fa-f]{6}",
        }
    )
    penwidth: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": -10000.0,
            "max_inclusive": 10000.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class EptsoType(Enum):
    PARABOLIC = "parabolic"
    CONSTANT = "constant"


class Eurocodetype(Enum):
    COMMON = "common"
    H = "H"
    RO = "RO"
    DK = "DK"
    S = "S"
    N = "N"
    FIN = "FIN"
    GB = "GB"
    D = "D"
    PL = "PL"
    TR = "TR"
    EST = "EST"
    LV = "LV"
    NL = "NL"
    B = "B"
    E = "E"
    N_A = "n/a"


@dataclass(kw_only=True)
class ExtlineType:
    class Meta:
        name = "extline_type"

    lines: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    base_point_on_dimension_line: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    extension_a: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e23,
        },
    )
    extension_b: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e23,
        },
    )
    offset_c: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e23,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class FdMatType(Enum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_65535 = 65535
    VALUE_1_1 = -1


class FillmodeType(Enum):
    AUTO_FILL = "auto_fill"
    COLOUR = "colour"
    NO_FILL = "no_fill"


class ForceLoadType(Enum):
    FORCE = "force"
    MOMENT = "moment"


@dataclass(kw_only=True)
class FoundationInsulationType:
    class Meta:
        name = "foundation_insulation_type"

    e_modulus: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    thickness: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0001,
            "max_inclusive": 10000.0,
        }
    )
    density: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    gamma_m_u: float = field(
        default=1.2,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1.0,
            "max_inclusive": 100000000.0,
        },
    )
    gamma_m_uas: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1.0,
            "max_inclusive": 100000000.0,
        },
    )
    limit_stress: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1.0,
            "max_inclusive": 100000000.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class FoundationPlinthType:
    class Meta:
        name = "foundation_plinth_type"

    a: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 10000.0,
        }
    )
    b: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 10000.0,
        }
    )
    h: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 10000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class FoundationsystemsType(Enum):
    SIMPLE = "simple"
    SURFACE_SUPPORT_GROUP = "surface_support_group"
    FROM_SOIL = "from_soil"


@dataclass(kw_only=True)
class GaDirectionRecord:
    class Meta:
        name = "ga_direction_record"

    factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    diagram: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class GlcLayer:
    class Meta:
        name = "glc_layer"

    material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,256}",
        }
    )
    thickness: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    theta: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.5707963267949,
        }
    )
    ex: float = field(
        metadata={
            "name": "Ex",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    ey: float = field(
        metadata={
            "name": "Ey",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    nuxy: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    gxy: float = field(
        metadata={
            "name": "Gxy",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    gxz: float = field(
        metadata={
            "name": "Gxz",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    gyz: float = field(
        metadata={
            "name": "Gyz",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    rho: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class GuidListType:
    class Meta:
        name = "guid_list_type"

    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class HalignType(Enum):
    CENTERED = "centered"
    VALUE_1ST_EXT_LINE = "1st_ext_line"
    VALUE_2ND_EXT_LINE = "2nd_ext_line"
    UNDER_1ST_EXT_LINE = "under_1st_ext_line"
    OVER_2ND_EXT_LINE = "over_2nd_ext_line"


class HorAlign(Enum):
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"


class InternalLineStyle(Enum):
    CONTINUOUS = "CONTINUOUS"
    DASH4 = "DASH4"
    DASH2 = "DASH2"
    DASH8 = "DASH8"
    DASH12 = "DASH12"
    CENTER4 = "CENTER4"
    CENTER2 = "CENTER2"
    CENTER8 = "CENTER8"
    CENTER12 = "CENTER12"
    DOT4 = "DOT4"
    DOT2 = "DOT2"
    DOT8 = "DOT8"
    DOT12 = "DOT12"
    SECTION4 = "SECTION4"
    SECTION2 = "SECTION2"
    SECTION8 = "SECTION8"
    SECTION12 = "SECTION12"
    DASHDOT4 = "DASHDOT4"
    DASHDOT2 = "DASHDOT2"
    DASHDOT8 = "DASHDOT8"
    DASHDOT12 = "DASHDOT12"


class LastStageValue(Enum):
    LAST_STAGE = "last_stage"


@dataclass(kw_only=True)
class LayerType:
    class Meta:
        name = "layer_type"

    name: str = field(
        default="0",
        metadata={
            "type": "Attribute",
            "pattern": r"[\t\n\r -�]{1,255}",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    hidden: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    protected: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class LcFinalCs(Enum):
    FINAL_CS = "final_cs"


class LcPileType(Enum):
    LDCASE_PILE = "ldcase_pile"


class LcPtcType(Enum):
    PTC_T0 = "ptc_t0"
    PTC_T8 = "ptc_t8"


class Ldcomblimitstate(Enum):
    ULTIMATE = "ultimate"
    CHARACTERISTIC = "characteristic"
    ACCIDENTAL = "accidental"
    SEISMIC = "seismic"
    QUASI_PERMANENT = "quasi-permanent"
    FREQUENT = "frequent"


class Ldcombmethod(Enum):
    VALUE = ""
    FALSE = "false"
    TRUE = "true"
    EN_1990_6_4_3_6_10_A_B = "EN 1990 6.4.3(6.10.a, b)"
    EN_1990_6_4_3_6_10 = "EN 1990 6.4.3(6.10)"
    CUSTOM = "custom"
    EN_1990_8_3_4_2_8_12 = "EN 1990 8.3.4.2 (8.12)"
    EN_1990_8_3_4_2_8_13 = "EN 1990 8.3.4.2 (8.13)"
    EN_1990_8_3_4_2_8_14 = "EN 1990 8.3.4.2 (8.14)"


class LdgroupDirectionType(Enum):
    NON_DIRECTIONAL = "non_directional"
    X = "x+"
    X_1 = "x-"
    Y = "y+"
    Y_1 = "y-"


class LdgroupRelation(Enum):
    VALUE = ""
    ALTERNATIVE = "alternative"
    SIMULTANEOUS = "simultaneous"
    ENTIRE = "entire"
    CUSTOM = "custom"


class LdgroupTmpeffect(Enum):
    GENERAL = "general"
    SNOW = "snow"
    WIND = "wind"


class LdposPosType(Enum):
    ON_CENTRIC_AXIS_SURFACE = "on_centric_axis/surface"
    ON_ECCENTRIC_AXIS_SURFACE = "on_eccentric_axis/surface"
    USER_DEFINED_ECCENTRICITY = "user_defined_eccentricity"


class LdposRefType(Enum):
    REFERENCE_AXIS = "reference_axis"
    CENTER_OF_GRAVITY = "center_of_gravity"
    SHEAR_CENTER = "shear_center"
    BOUNDING_RECTANGLE = "bounding_rectangle"


class LengthunitType(Enum):
    MM = "mm"
    CM = "cm"
    DM = "dm"
    M = "m"
    INCH = "inch"
    FEET = "feet"
    YD = "yd"


@dataclass(kw_only=True)
class LevelPointType:
    class Meta:
        name = "level_point_type"

    x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    z_top: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    z_bottom: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LinetypeType:
    class Meta:
        name = "linetype_type"

    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    distances: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
            "tokens": True,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LnfoundationRefType:
    class Meta:
        name = "lnfoundation_ref_type"

    ref_wall: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    ref_slab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    ref_support: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class LoadDirType(Enum):
    CONSTANT = "constant"
    CHANGING = "changing"


class Loadcasedurationtype(Enum):
    PERMANENT = "permanent"
    LONG_TERM = "long-term"
    MEDIUM_TERM = "medium-term"
    SHORT_TERM = "short-term"
    INSTANTANEOUS = "instantaneous"


class LoadcasetypeType(Enum):
    STATIC = "static"
    DEAD_LOAD = "dead_load"
    SHRINKAGE = "shrinkage"
    SEIS_MAX = "seis_max"
    SEIS_SXP = "seis_sxp"
    SEIS_SXM = "seis_sxm"
    SEIS_SYP = "seis_syp"
    SEIS_SYM = "seis_sym"
    SOIL_DEAD_LOAD = "soil_dead_load"
    PRESTRESSING = "prestressing"
    FIRE = "fire"
    DEVIATION = "deviation"
    NOTIONAL = "notional"
    PILE = "pile"
    DIAPHRAGM = "diaphragm"


class Loadcombtype(Enum):
    ULTIMATE_ORDINARY = "ultimate_ordinary"
    ULTIMATE_ACCIDENTAL = "ultimate_accidental"
    ULTIMATE_SEISMIC = "ultimate_seismic"
    SERVICEABILITY_CHARACTERISTIC = "serviceability_characteristic"
    SERVICEABILITY_QUASI_PERMANENT = "serviceability_quasi_permanent"
    SERVICEABILITY_FREQUENT = "serviceability_frequent"
    SERVICEABILITY = "serviceability"


class MethodAcc(Enum):
    FACTORLESS = "factorless"
    GAMMA_A = "Gamma_A"


class MethodIs(Enum):
    GENERAL = "general"
    HIGHLIGHTED = "highlighted"
    SIMULTANEOUS = "simultaneous"


class MethodPer(Enum):
    FACTORLESS = "factorless"
    GAMMA_G_SUP = "Gamma_G_Sup"
    GAMMA_G_INF = "Gamma_G_Inf"
    KSI_GAMMA_G_SUP = "Ksi_*_Gamma_G_Sup"
    GAMMA_G_SUP_ACCIDENTAL = "Gamma_G_Sup_Accidental"
    GAMMA_G_INF_ACCIDENTAL = "Gamma_G_Inf_Accidental"


class MethodSeis(Enum):
    FACTORLESS = "factorless"
    GAMMA_S = "Gamma_S"


class MethodSs(Enum):
    MANDATORY = "mandatory"
    OPTIONAL = "optional"
    DEACTIVATED = "deactivated"


class MethodStr(Enum):
    FACTORLESS = "factorless"
    GAMMA_P = "Gamma_P"
    GAMMA_P_ACCIDENTAL = "Gamma_P_Accidental"


class MethodTmp(Enum):
    FACTORLESS = "factorless"
    GAMMA_Q = "Gamma_Q"
    PSI0 = "Psi0"
    PSI1 = "Psi1"
    PSI2 = "Psi2"
    GAMMA_Q_PSI0 = "Gamma_Q_*_Psi0"
    GAMMA_Q_PSI1 = "Gamma_Q_*_Psi1"
    GAMMA_Q_PSI2 = "Gamma_Q_*_Psi2"


class ModificationType(Enum):
    ADDED = "added"
    MODIFIED = "modified"


class MotionType(Enum):
    MOTION = "motion"
    ROTATION = "rotation"


class MrmType(Enum):
    EN1992_1_1_5_3_2_2_3 = "EN1992-1-1 5.3.2.2(3)"
    EN1992_1_1_5_3_2_2_4 = "EN1992-1-1 5.3.2.2(4)"


@dataclass(kw_only=True)
class NoshearAutoType:
    class Meta:
        name = "noshear_auto_type"

    connected_structure: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    inactive: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class OptionalMaterialAttribs:
    class Meta:
        name = "optional_material_attribs"

    mass: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    e_0: float = field(
        metadata={
            "name": "E_0",
            "type": "Attribute",
            "required": True,
        }
    )
    e_1: float = field(
        metadata={
            "name": "E_1",
            "type": "Attribute",
            "required": True,
        }
    )
    e_2: float = field(
        metadata={
            "name": "E_2",
            "type": "Attribute",
            "required": True,
        }
    )
    nu_0: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    nu_1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    nu_2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    alfa_0: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    alfa_1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    alfa_2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    g_0: float = field(
        metadata={
            "name": "G_0",
            "type": "Attribute",
            "required": True,
        }
    )
    g_1: float = field(
        metadata={
            "name": "G_1",
            "type": "Attribute",
            "required": True,
        }
    )
    g_2: float = field(
        metadata={
            "name": "G_2",
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class Paneltype2(Enum):
    CONCRETE = "concrete"
    TIMBER = "timber"


@dataclass(kw_only=True)
class PathDivisionLengtType:
    class Meta:
        name = "path_division_lengt_type"

    value: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 1000.0,
        }
    )


@dataclass(kw_only=True)
class PathDivisionNumberType:
    class Meta:
        name = "path_division_number_type"

    value: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 1000,
        }
    )


@dataclass(kw_only=True)
class PcNonrigidConnectionType:
    class Meta:
        name = "pc_nonrigid_connection_type"

    predefined_rigidity: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,40}",
        }
    )
    start_point_connected: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    end_point_connected: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class PePhaseType(Enum):
    SIN = "sin"
    COS = "cos"


@dataclass(kw_only=True)
class PheType:
    class Meta:
        name = "phe_type"

    offset: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    shrink: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class PiletypeType(Enum):
    DRIVEN_DISPLACEMENT = "driven_displacement"
    DRIVEN_JETTED = "driven_jetted"
    BORED = "bored"


@dataclass(kw_only=True)
class Plasticity3DForceRecord:
    class Meta:
        name = "plasticity3d_force_record"

    force_x_neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    force_x_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    force_y_neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    force_y_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    force_z_neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    force_z_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PlasticityType:
    class Meta:
        name = "plasticity_type"

    neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PlasticityType2:
    class Meta:
        name = "plasticity_type2"

    neg: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    pos: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PlasticityType3D:
    class Meta:
        name = "plasticity_type_3d"

    x_neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    x_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    y_neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    y_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    z_neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    z_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PointType1D:
    class Meta:
        name = "point_type_1d"

    x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class PointstyleType(Enum):
    CROSS = "cross"
    PLUS_SIGN = "plus_sign"
    DIAMOND = "diamond"
    SQUARE = "square"
    DOT = "dot"


class PriorityType(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"


class PshDiameterValue(Enum):
    VALUE_0_025 = 0.025
    VALUE_0_032 = 0.032
    VALUE_0_040 = "0.040"


class PtcJackingSide(Enum):
    START = "start"
    END = "end"
    START_THEN_END = "start_then_end"
    END_THEN_START = "end_then_start"


@dataclass(kw_only=True)
class PtcLosses:
    class Meta:
        name = "ptc_losses"

    curvature_coefficient: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    wobble_coefficient: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    anchorage_set_slip: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    elastic_shortening: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10000000.0,
        }
    )
    creep_stress: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10000000.0,
        }
    )
    shrinkage_stress: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10000000.0,
        }
    )
    relaxation_stress: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10000000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PtcManufacturingType:
    class Meta:
        name = "ptc_manufacturing_type"

    positions: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
            "tokens": True,
        },
    )
    shift_x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    shift_z: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PtcShapeEnd:
    class Meta:
        name = "ptc_shape_end"

    z: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    tangent: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1.5533430342749532,
            "max_inclusive": 1.5533430342749532,
        }
    )
    prior_inflection_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PtcShapeInner:
    class Meta:
        name = "ptc_shape_inner"

    pos: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_exclusive": 1.0,
        }
    )
    z: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    tangent: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1.5533430342749532,
            "max_inclusive": 1.5533430342749532,
        }
    )
    prior_inflection_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PtcShapeStart:
    class Meta:
        name = "ptc_shape_start"

    z: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    tangent: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1.5533430342749532,
            "max_inclusive": 1.5533430342749532,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PtfoundationRefType:
    class Meta:
        name = "ptfoundation_ref_type"

    ref_slab: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    ref_support: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class Quadrant(Enum):
    VALUE_0 = "0"
    VALUE_90 = "90"
    VALUE_180 = "180"
    VALUE_270 = "270"


class RcsmType(Enum):
    VECCHIO_1 = "Vecchio 1"
    VECCHIO_2 = "Vecchio 2"
    CERVERA = "Cervera"
    MODEL_CODE_2010 = "Model Code 2010"
    EN_1992_1_1_2023 = "EN 1992-1-1:2023"


class RecPosType(Enum):
    TOP_LEFT = "top_left"
    TOP_CENTER = "top_center"
    TOP_RIGHT = "top_right"
    CENTER_LEFT = "center_left"
    CENTER_CENTER = "center_center"
    CENTER_RIGHT = "center_right"
    BOTTOM_LEFT = "bottom_left"
    BOTTOM_CENTER = "bottom_center"
    BOTTOM_RIGHT = "bottom_right"


@dataclass(kw_only=True)
class ReferenceType:
    class Meta:
        name = "reference_type"

    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ResultantType:
    class Meta:
        name = "resultant_type"

    val: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RlBaseType:
    class Meta:
        name = "rl_base_type"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )


class RoofType(Enum):
    FLAT = "flat"
    LEAN_TO = "lean-to"
    RIDGE = "ridge"


class ScriptType(Enum):
    DEFAULT = "default"
    ARABIC = "Arabic"
    BALTIC = "Baltic"
    CE = "CE"
    CYRILLIK = "Cyrillik"
    GREEK = "Greek"
    HEBREW = "Hebrew"
    OEM_DOS = "OEM/DOS"
    SYMBOL = "symbol"
    THAI = "Thai"
    TURKISH = "Turkish"
    VIETNAMESE = "Vietnamese"
    WESTERN = "Western"


class Sectiontype2(Enum):
    CUSTOM = "custom"
    I = "I"
    U = "U"
    RECT = "rect"
    CIRCLE = "circle"


@dataclass(kw_only=True)
class SegmentpositionType:
    class Meta:
        name = "segmentposition_type"

    start: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    end: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class SeismicGroundType(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    S1_S2_6_20M = "S1/S2_6-20m"
    S1_S2_20_35M_A = "S1/S2_20-35mA"
    S1_S2_35_60M_A = "S1/S2_35-60mA"


class SeismicStructureType(Enum):
    BUILDING = "building"
    BRIDGE = "bridge"
    OTHERS = "others"


@dataclass(kw_only=True)
class ServiceClassFactors:
    class Meta:
        name = "service_class_factors"

    kdef: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    kmod_permanent: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    kmod_long_term: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    kmod_medium_term: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    kmod_short_term: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    kmod_instantaneous: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ServiceClassKdefs:
    class Meta:
        name = "service_class_kdefs"

    service_class_0: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    service_class_1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    service_class_2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 100000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class SfRcFace(Enum):
    TOP = "top"
    BOTTOM = "bottom"


@dataclass(kw_only=True)
class SfactorType:
    class Meta:
        name = "sfactor_type"

    sc: float = field(
        metadata={
            "name": "Sc",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )
    sf: float = field(
        metadata={
            "name": "Sf",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )
    sq: float = field(
        metadata={
            "name": "Sq",
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SffoundationRefType:
    class Meta:
        name = "sffoundation_ref_type"

    ref_slab: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    ref_support: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ShearControlAutoType:
    class Meta:
        name = "shear_control_auto_type"

    connected_structure: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class ShellForceType(Enum):
    INTEGRATION = "integration"
    SMOOTHED = "smoothed"
    MAX = "max"


class ShellModelType(Enum):
    NONE = "none"
    SIMPLE = "simple"
    COMPLEX = "complex"


@dataclass(kw_only=True)
class SimpleConnectivityType:
    class Meta:
        name = "simple_connectivity_type"

    m_x: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    m_x_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    m_y: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    m_y_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    m_z: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    m_z_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    r_x: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    r_x_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    r_y: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    r_y_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    r_z: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    r_z_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    v_x: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    v_x_release: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000000.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SjBoltlineType:
    class Meta:
        name = "sj_boltline_type"

    distance: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[!-~]{1}[ -~]{0,49}",
        }
    )
    from_value: str = field(
        metadata={
            "name": "from",
            "type": "Attribute",
            "required": True,
            "pattern": r"[!-~]{1}[ -~]{0,49}",
        }
    )
    bolts: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[!-~]{1}[ -~]{0,49}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class SjComponentValues(Enum):
    BUCKLING = "buckling"
    ENDPLATE = "endplate"
    HAUNCH_TOP = "haunch_top"
    HAUNCH_BOTTOM = "haunch_bottom"
    STIFFENER_TOP = "stiffener_top"
    STIFFENER_BOTTOM = "stiffener_bottom"
    STIFFENER_DIAGONAL = "stiffener_diagonal"
    STIFFENER_GENERAL = "stiffener_general"
    STIFFENER_TRIANGULAR = "stiffener_triangular"
    FIN_PLATE = "fin_plate"
    SPLICE_WEB = "splice_web"
    SPLICE_FLANGE_BOTTOM = "splice_flange_bottom"
    SPLICE_FLANGE_TOP = "splice_flange_top"
    COVER_PLATE = "cover_plate"
    HEEL = "heel"
    GUSSET_PLATE = "gusset_plate"
    CHAMPFER_PLATE = "champfer_plate"
    BACKING_PLATE = "backing_plate"
    SUPPORT_PLATE = "support_plate"
    CONCRETE = "concrete"
    NOTCH = "notch"
    GAP = "gap"
    ECCENTRICITY = "eccentricity"
    CUT = "cut"
    BOLTS = "bolts"
    WELDS = "welds"
    GEOMETRY = "geometry"
    ENDPLATE_BOLTS = "endplate_bolts"
    ENDPLATE_WELDS = "endplate_welds"
    ENDPLATE_WELDS_AT_BEAM = "endplate_welds_at_beam"
    ENDPLATE_WELDS_AT_COLUMN = "endplate_welds_at_column"
    SPLICE_WEB_BOLTS = "splice_web_bolts"
    FLANGE_BOLTS = "flange_bolts"
    SPLICE_WEB_WELD = "splice_web_weld"
    FLANGE_SPLICE_WELD = "flange_splice_weld"
    FIN_BOLTS = "fin_bolts"
    FIN_WELDS = "fin_welds"
    HEEL_WELDS = "heel_welds"
    COVER_WELDS = "cover_welds"
    SUPPORT_PLATE_WELDS = "support_plate_welds"
    STIFFENER_WELDS = "stiffener_welds"
    CALCULATION = "calculation"
    ANCHOR_GEOMETRY = "anchor_geometry"
    ANCHOR_CALCULATIONS = "anchor_calculations"
    CALCULATION_PARAMETERS = "calculation_parameters"


class SjConnectedBarType(Enum):
    COLUMNS_END = "columns_end"
    COLUMN = "column"
    TOP_COLUMN = "top_column"
    BOTTOM_COLUMN = "bottom_column"
    BEAM = "beam"
    BEAM_1 = "beam_1"
    BEAM_2 = "beam_2"
    BRACE_1 = "brace_1"
    BRACE_2 = "brace_2"
    CHORD = "chord"
    JOINT = "joint"
    FOUNDATION = "foundation"
    ANCHOR_CONCRETE_INTERACTION = "anchor-concrete_interaction"


class SjDatatypeNames(Enum):
    BUCKLING_LC_Y = "buckling_lc_y"
    BUCKLING_LC_Z = "buckling_lc_z"
    BUCKLING_X_Y = "buckling_x_y"
    BUCKLING_X_Z = "buckling_x_z"
    BRACE_CHORD_DISTANCE = "brace_chord_distance"
    BRACE_CUT_TYPE = "brace_cut_type"
    BRACE_CUT_DISTANCE = "brace_cut_distance"
    BRACE_ECCENTRICITY = "brace_eccentricity"
    BRACE_OVERLAPPED = "brace_overlapped"
    BRACE_OVERLAPPED_WELD = "brace_overlapped_weld"
    CALC_TENSION_BOLTROWS_FOR_SHEAR = "calc_tension_boltrows_for_shear"
    FOUNDATION_BETA = "foundation_beta"
    FOUNDATION_CFD = "foundation_cfd"
    FOUNDATION_CMIN = "foundation_cmin"
    FOUNDATION_CRACKED = "foundation_cracked"
    FOUNDATION_EY = "foundation_ey"
    FOUNDATION_EZ = "foundation_ez"
    FOUNDATION_FAILURE_CHECK = "foundation_failure_check"
    FOUNDATION_GAMMA_MC = "foundation_gamma_mc"
    FOUNDATION_GAMMA_MP = "foundation_gamma_mp"
    FOUNDATION_GAMMA_MSP = "foundation_gamma_msp"
    FOUNDATION_H = "foundation_h"
    FOUNDATION_HMIN = "foundation_hmin"
    FOUNDATION_IGNORE_CONE_FAILURE = "foundation_ignore_cone_failure"
    FOUNDATION_IGNORE_SPLIT_FAILURE = "foundation_ignore_split_failure"
    FOUNDATION_KCR = "foundation_kcr"
    FOUNDATION_KJ = "foundation_kj"
    FOUNDATION_KUCR = "foundation_kucr"
    FOUNDATION_L = "foundation_l"
    FOUNDATION_MATERIAL = "foundation_material"
    FOUNDATION_SMIN = "foundation_smin"
    FOUNDATION_U = "foundation_u"
    FOUNDATION_W = "foundation_w"
    NOTCH_HB = "notch_hb"
    NOTCH_HT = "notch_ht"
    NOTCH_EB = "notch_eb"
    NOTCH_ET = "notch_et"
    GAP_SIZE = "gap_size"
    PLATE_APPLY = "plate_apply"
    PLATE_MATERIAL = "plate_material"
    PLATE_TP = "plate_tp"
    PLATE_BP = "plate_bp"
    PLATE_HP = "plate_hp"
    PLATE_LENGTH = "plate_length"
    PLATE_AUX_PARAM1 = "plate_aux_param1"
    PLATE_AUX_PARAM2 = "plate_aux_param2"
    PLATE_AUX_PARAM3 = "plate_aux_param3"
    PLATE_AUX_PARAM4 = "plate_aux_param4"
    PLATE_AUX_PARAM5 = "plate_aux_param5"
    PLATE_AUX_PARAM6 = "plate_aux_param6"
    PLATE_AUX_PARAM7 = "plate_aux_param7"
    PLATE_AUX_PARAM8 = "plate_aux_param8"
    BOLT_TYPE = "bolt_type"
    BOLT_QUALITY = "bolt_quality"
    BOLT_PRESTRESSED = "bolt_prestressed"
    BOLT_FLIP = "bolt_flip"
    BOLT_WASHER_AT_NUT = "bolt_washer_at_nut"
    BOLT_WASHER_AT_HEAD = "bolt_washer_at_head"
    ANCHOR_DIAMETER = "anchor_diameter"
    ANCHOR_QUALITY = "anchor_quality"
    ANCHOR_SURFACE = "anchor_surface"
    ANCHOR_M = "anchor_m"
    ANCHOR_TB = "anchor_tb"
    ANCHOR_USE_MAX_OF_FTRD = "anchor_use_max_of_ftrd"
    ANCHOR_FTRD = "anchor_ftrd"
    ANCHOR_TYPE = "anchor_type"
    ANCHOR_SHAPE = "anchor_shape"
    ANCHOR_H = "anchor_h"
    ANCHOR_LHORIZ = "anchor_lhoriz"
    ANCHOR_RBEND = "anchor_rbend"
    ANCHOR_CHECKADH = "anchor_checkadh"
    ANCHOR_DH = "anchor_dh"
    ANCHOR_CFD = "anchor_cfd"
    ANCHOR_SUITABILITY_TEST = "anchor_suitability_test"
    BOLT_GROUP_NCOL = "bolt_group_ncol"
    BOLT_GROUP_NROW = "bolt_group_nrow"
    BOLT_GROUP_C1 = "bolt_group_c1"
    BOLT_GROUP_C2 = "bolt_group_c2"
    BOLT_GROUP_C3 = "bolt_group_c3"
    BOLT_GROUP_C4 = "bolt_group_c4"
    BOLT_GROUP_E0 = "bolt_group_e0"
    BOLT_GROUP_E = "bolt_group_e"
    BOLT_GROUP_E1 = "bolt_group_e1"
    BOLT_GROUP_E2 = "bolt_group_e2"
    BOLT_GROUP_ROWS = "bolt_group_rows"
    WELD_TYPE = "weld_type"
    WELD_S = "weld_s"
    WELD_A = "weld_a"
    WELD_AFHT = "weld_afht"
    WELD_AWHT = "weld_awht"
    WELD_AF1 = "weld_af1"
    WELD_AFT = "weld_aft"
    WELD_AW_L = "weld_aw(l)"
    WELD_AWR = "weld_awr"
    WELD_AF_B = "weld_af(b)"
    WELD_AF4 = "weld_af4"
    WELD_AWHB = "weld_awhb"
    WELD_AFHB = "weld_afhb"
    WELD_AWH_TOP = "weld_awh_top"
    WELD_AWH_BOTTOM = "weld_awh_bottom"
    WELD_AF1_BACK = "weld_af1_back"
    WELD_AFT_BACK = "weld_aft_back"
    WELD_AFW_BACK = "weld_afw_back"
    WELD_AFB_BACK = "weld_afb_back"
    WELD_AF4_BACK = "weld_af4_back"
    WELD_LENGTH = "weld_length"
    WELD_EDGES = "weld_edges"
    WELD_BUTTERING = "weld_buttering"
    WELD_PREHEATING = "weld_preheating"
    WELD_FILLER_MATERIAL = "weld_filler_material"
    WELD_FILLER_MATERIAL_S = "weld_filler_material_s"
    WELD_FILLER_MATERIAL_FHT = "weld_filler_material_fht"
    WELD_FILLER_MATERIAL_WHT = "weld_filler_material_wht"
    WELD_FILLER_MATERIAL_F1 = "weld_filler_material_f1"
    WELD_FILLER_MATERIAL_FT = "weld_filler_material_ft"
    WELD_FILLER_MATERIAL_W_L = "weld_filler_material_w(l)"
    WELD_FILLER_MATERIAL_WR = "weld_filler_material_wr"
    WELD_FILLER_MATERIAL_F_B = "weld_filler_material_f(b)"
    WELD_FILLER_MATERIAL_F4 = "weld_filler_material_f4"
    WELD_FILLER_MATERIAL_WHB = "weld_filler_material_whb"
    WELD_FILLER_MATERIAL_FHB = "weld_filler_material_fhb"
    WELD_TOP_FILLER_MATERIAL_WH = "weld_top_filler_material_wh"
    WELD_BOTTOM_FILLER_MATERIAL_WH = "weld_bottom_filler_material_wh"
    WELD_FILLER_MATERIAL_F1_BACK = "weld_filler_material_f1_back"
    WELD_FILLER_MATERIAL_FT_BACK = "weld_filler_material_ft_back"
    WELD_FILLER_MATERIAL_FW_BACK = "weld_filler_material_fw_back"
    WELD_FILLER_MATERIAL_FB_BACK = "weld_filler_material_fb_back"
    WELD_FILLER_MATERIAL_F4_BACK = "weld_filler_material_f4_back"


@dataclass(kw_only=True)
class SjForceType:
    class Meta:
        name = "sj_force_type"

    n: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -100000000.0,
            "max_inclusive": 100000000.0,
        },
    )
    t_y: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -100000000.0,
            "max_inclusive": 100000000.0,
        },
    )
    t_z: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -100000000.0,
            "max_inclusive": 100000000.0,
        },
    )
    m_x: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -100000000.0,
            "max_inclusive": 100000000.0,
        },
    )
    m_y: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -100000000.0,
            "max_inclusive": 100000000.0,
        },
    )
    m_z: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -100000000.0,
            "max_inclusive": 100000000.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SlabStiffnessRecord:
    class Meta:
        name = "slab_stiffness_record"

    bending_1_1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        }
    )
    bending_2_2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        }
    )
    bending_1_2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        }
    )
    membran_1_1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        }
    )
    membran_2_2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        }
    )
    membran_1_2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        }
    )
    shear_1_3: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        }
    )
    shear_2_3: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 10.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class SlabfoundationsystemsType(Enum):
    SURFACE_SUPPORT_GROUP = "surface_support_group"
    FROM_SOIL = "from_soil"


class Slabtype2(Enum):
    PLATE = "plate"
    WALL = "wall"


@dataclass(kw_only=True)
class SpecLoadCaseItem:
    class Meta:
        name = "spec_load_case_item"

    gamma: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SpectraRecordType:
    class Meta:
        name = "spectra_record_type"

    t: float = field(
        metadata={
            "name": "T",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    sd: float = field(
        metadata={
            "name": "Sd",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class SrfTreatmentType(Enum):
    MANUAL = "manual"
    AUTO_BASE_NET = "auto_base_net"
    AUTO_ADDITIONAL = "auto_additional"
    AUTO_CRACK_WIDTH = "auto_crack_width"


class SsrfTreatment(Enum):
    MANUAL = "manual"
    AUTO = "auto"


@dataclass(kw_only=True)
class StandardSpectraType:
    class Meta:
        name = "standard_spectra_type"

    ag: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    td: float = field(
        metadata={
            "name": "TD",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    q: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    type_value: int = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 2,
        }
    )
    s: float = field(
        metadata={
            "name": "S",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    tb: float = field(
        metadata={
            "name": "TB",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    tc: float = field(
        metadata={
            "name": "TC",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    beta: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class Standardtype(Enum):
    EC = "EC"
    EC_G2 = "EC_G2"
    GENERAL = "general"
    N_A = "n/a"


@dataclass(kw_only=True)
class StartEndType:
    class Meta:
        name = "start_end_type"

    start: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        }
    )
    end: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class Steelmadetype(Enum):
    ROLLED = "rolled"
    COLD_WORKED = "cold_worked"
    WELDED = "welded"


@dataclass(kw_only=True)
class StiffnessMatrix2Type:
    class Meta:
        name = "stiffness_matrix_2_type"

    xz: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    yz: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class StiffnessMatrix4Type:
    class Meta:
        name = "stiffness_matrix_4_type"

    xx: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    xy: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    yy: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    gxy: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class StiffnessMaxReached(Enum):
    VALUE_6_E66 = 6e66


@dataclass(kw_only=True)
class StratumType:
    class Meta:
        name = "stratum_type"

    material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    colour: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Fa-f]{6}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class StrengthType(Enum):
    BRICK_ONLY = "brick_only"
    MASONRY = "masonry"


class StudrailPatterns(Enum):
    RADIAL = "radial"
    ORTHOGONAL = "orthogonal"
    SEMI_ORTHOGONAL = "semi-orthogonal"


@dataclass(kw_only=True)
class TdaCreepComplianceGeneral:
    class Meta:
        name = "tda_creep_compliance_general"

    record: list[TdaCreepComplianceGeneral.Record] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Record:
        t: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 10000000.0,
            }
        )
        j: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1.0,
                "max_inclusive": 100000.0,
            }
        )


@dataclass(kw_only=True)
class TdaCreepProny:
    class Meta:
        name = "tda_creep_prony"

    record: list[TdaCreepProny.Record] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )

    @dataclass(kw_only=True)
    class Record:
        j: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": -100000000.0,
                "max_inclusive": 100000000.0,
            }
        )
        tau: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": -100000000.0,
                "max_inclusive": 100000000.0,
            }
        )


@dataclass(kw_only=True)
class ThDiagramRecord:
    class Meta:
        name = "th_diagram_record"

    t: float = field(
        metadata={
            "name": "T",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
        }
    )
    value: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1.0,
            "max_inclusive": 1.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ThreeGuidListType:
    class Meta:
        name = "three_guid_list_type"

    first: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    second: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    third: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TimberFactorsType:
    class Meta:
        name = "timber_factors_type"

    gamma_m_u: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    gamma_m_as: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    kdef_u: float = field(
        metadata={
            "name": "kdef_U",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    kdef_sq: float = field(
        metadata={
            "name": "kdef_Sq",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    kdef_sf: float = field(
        metadata={
            "name": "kdef_Sf",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    kdef_sc: float = field(
        metadata={
            "name": "kdef_Sc",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    service_class: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0,
            "max_inclusive": 2,
        }
    )
    system_factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TrussLimitType:
    class Meta:
        name = "truss_limit_type"

    value: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )


@dataclass(kw_only=True)
class TsIndexedVertexType:
    class Meta:
        name = "ts_indexed_vertex_type"

    index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class TsType(Enum):
    HINTON = "Hinton"
    VECCHIO = "Vecchio"
    LINEAR = "Linear"
    CERVERA = "Cervera"


@dataclass(kw_only=True)
class TwoGuidListType:
    class Meta:
        name = "two_guid_list_type"

    first: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    second: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class UserfilterType:
    class Meta:
        name = "userfilter_type"

    members: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            "tokens": True,
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{0,15}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class ValignType(Enum):
    ABOVE = "above"
    OUTSIDE = "outside"


class VerAlign(Enum):
    TOP = "top"
    CENTER = "center"
    BOTTOM = "bottom"


class Viewtype2(Enum):
    VALUE_2D = "2d"
    VALUE_3D = "3d"
    STOREY = "storey"


class Visiblelinetype(Enum):
    LINE = "line"
    POLYLINE = "polyline"
    SPLINE = "spline"


@dataclass(kw_only=True)
class WaterLevelType:
    class Meta:
        name = "water_level_type"

    colour: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Fa-f]{6}",
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,256}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


class WireProfileType(Enum):
    SMOOTH = "smooth"
    RIBBED = "ribbed"


@dataclass(kw_only=True)
class WlNtType:
    class Meta:
        name = "wl_nt_type"

    mult_factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class WlStType:
    class Meta:
        name = "wl_st_type"

    suction_factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    turbulence: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class WlTType:
    class Meta:
        name = "wl_t_type"

    mult_factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    turbulence: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EcG2HorizontalSpectraType:
    class Meta:
        name = "EC_G2_horizontal_spectra_type"

    amplification_factors: (
        None | EcG2HorizontalSpectraType.AmplificationFactors
    ) = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    site_category: None | EcG2HorizontalSpectraType.SiteCategory = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    salpha_rp: float = field(
        metadata={
            "name": "SalphaRP",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    sbeta_rp: float = field(
        metadata={
            "name": "SbetaRP",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    ft: float = field(
        metadata={
            "name": "FT",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    fa: float = field(
        metadata={
            "name": "FA",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    chi: float = field(
        metadata={
            "name": "Chi",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    ta: float = field(
        metadata={
            "name": "TA",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    td: float = field(
        metadata={
            "name": "TD",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    beta_h: float = field(
        metadata={
            "name": "BetaH",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class AmplificationFactors:
        falpha: float = field(
            metadata={
                "name": "Falpha",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 10.0,
            }
        )
        fbeta: float = field(
            metadata={
                "name": "Fbeta",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 10.0,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class SiteCategory:
        type_value: EcG2SeismicGroundType = field(
            metadata={
                "name": "type",
                "type": "Attribute",
                "required": True,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class EcG2UniqueSpectraType:
    class Meta:
        name = "EC_G2_unique_spectra_type"

    record: list[EcG2SpectraRecordType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 127,
        },
    )
    start_sr: float = field(
        metadata={
            "name": "start_Sr",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 20.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class AncType:
    class Meta:
        name = "anc_type"

    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    r: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    calculated_automatically: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    length: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 3.403e35,
        }
    )
    automatically_handled: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ArrowType:
    class Meta:
        name = "arrow_type"

    type_value: ArrowtypeType = field(
        default=ArrowtypeType.TICK,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    size: float = field(
        default=0.005,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e23,
        },
    )
    penwidth: float = field(
        default=0.00018,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e23,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BarEndLibType:
    class Meta:
        name = "bar_end_lib_type"

    connectivity: SimpleConnectivityType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BarStiffnessFactors:
    class Meta:
        name = "bar_stiffness_factors"

    factors: list[BarStiffnessFactorRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 10,
            "max_occurs": 10,
        },
    )


@dataclass(kw_only=True)
class BoltDataType:
    class Meta:
        name = "bolt_data_type"

    bolt_length: list[BoltLengthType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )
    family: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,40}",
        }
    )
    d: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    pitch: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    stress_area: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10000.0,
        }
    )
    bolt_b: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    bolt_c: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    bolt_ds: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    bolt_da: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    bolt_dw: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    bolt_e: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    bolt_k: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    bolt_s: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    bolt_r: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    nut_m: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    nut_e: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    nut_s: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    washer_thickness: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BoreholeType:
    class Meta:
        name = "borehole_type"

    whole_level_data: None | AllLevelsType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    final_ground_level: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000000.0,
            "max_inclusive": 10000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CltDatatype:
    class Meta:
        name = "clt_datatype"

    default_kdef: ServiceClassKdefs = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    layer: list[CltLayer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    manufacturer: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,40}",
        }
    )
    r33: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 1.0,
        }
    )
    r66: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 1.0,
        }
    )
    r77: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 1.0,
        }
    )
    r88: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 1.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ColumnCorbelType:
    class Meta:
        name = "column_corbel_type"

    connectable_parts: None | ThreeGuidListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    connectivity: ConnectivityType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    base_column: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    complex_material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    made: Steelmadetype = field(
        default=Steelmadetype.ROLLED,
        metadata={
            "type": "Attribute",
        },
    )
    complex_section: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    pos: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    alpha: Quadrant = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    d: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        },
    )
    l: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    e: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -10.0,
            "max_inclusive": 10.0,
        }
    )
    x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -10.0,
            "max_inclusive": 10.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ComplexCompositeType:
    class Meta:
        name = "complex_composite_type"

    composite_section: list[CompositeSectionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ComplexMaterialType:
    class Meta:
        name = "complex_material_type"

    material: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CompositePropType:
    class Meta:
        name = "composite_prop_type"

    name: CompositePropName = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ConcretePlAttribs:
    class Meta:
        name = "concrete_pl_attribs"

    elasto_plastic_behaviour: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    plastic_hardening: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    concrete_crushing: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    concrete_crushing_option: CcType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    tension_strength: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    tension_stiffening: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    tension_stiffening_option: TsType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    tension_stiffening_param: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    reduced_compression_strength: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    reduced_compression_strength_option: RcsmType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    reduced_compression_strength_param: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 500.0,
        }
    )
    reduced_transverse_shear_stiffnes: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    ultimate_strain: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    reduced_yield_stress: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    reduced_yield_stress_param: float = field(
        default=0.05,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    hardening_in_rebars: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ConnSideType:
    class Meta:
        name = "conn_side_type"

    non_rigid_connection: None | PcNonrigidConnectionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CoverlistType:
    class Meta:
        name = "coverlist_type"

    cover: list[CoverlistType.Cover] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 5,
            "max_occurs": 6,
        },
    )

    @dataclass(kw_only=True)
    class Cover:
        guid: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            }
        )
        stage: int = field(
            default=1,
            metadata={
                "type": "Attribute",
                "min_inclusive": 1,
                "max_inclusive": 32767,
            },
        )
        end_stage: LastStageValue | int = field(
            default=LastStageValue.LAST_STAGE,
            metadata={
                "type": "Attribute",
                "min_inclusive": 1,
                "max_inclusive": 32767,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class CsLcType:
    class Meta:
        name = "cs_lc_type"

    s_factors: None | SfactorType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    case: str | LcPtcType | LcPileType = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )
    partitioning: CsPartType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Ec040StandardSpectraType:
    class Meta:
        name = "ec040_standard_spectra_type"

    ag: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    td: float = field(
        metadata={
            "name": "TD",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    q: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    tc: Ec40TcType = field(
        metadata={
            "name": "TC",
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EccValueType:
    class Meta:
        name = "ecc_value_type"

    x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    z: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    reference_point: BeamposType = field(
        default=BeamposType.CENTER_OF_GRAVITY,
        metadata={
            "type": "Attribute",
        },
    )
    rectangle_position: RecPosType = field(
        default=RecPosType.CENTER_CENTER,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EfDiagramType:
    class Meta:
        name = "ef_diagram_type"

    record: list[ThDiagramRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    direction: Direction2DType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    start_value: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1.0,
            "max_inclusive": 1.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EfLcaseRecord:
    class Meta:
        name = "ef_lcase_record"

    factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    diagram: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class FillType:
    class Meta:
        name = "fill_type"

    mode: FillmodeType = field(
        default=FillmodeType.AUTO_FILL,
        metadata={
            "type": "Attribute",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class FontType:
    class Meta:
        name = "font_type"

    font: str = field(
        default="Tahoma",
        metadata={
            "type": "Attribute",
        },
    )
    script: ScriptType = field(
        default=ScriptType.WESTERN,
        metadata={
            "type": "Attribute",
        },
    )
    size: float = field(
        default=0.004,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 1e23,
        },
    )
    width: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        },
    )
    slant: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -80.0,
            "max_inclusive": 80.0,
        },
    )
    bold: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    italic: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    underline: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    strikethrough: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class GaCombinationType:
    class Meta:
        name = "ga_combination_type"

    direction_x: GaDirectionRecord = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction_y: GaDirectionRecord = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction_z: GaDirectionRecord = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    dt: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class GaDiagramType:
    class Meta:
        name = "ga_diagram_type"

    record: list[ThDiagramRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    direction: Direction2DType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class GlcDatatype:
    class Meta:
        name = "glc_datatype"

    layer: list[GlcLayer] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    group: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,40}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LdgroupRelationRecordType:
    class Meta:
        name = "ldgroup_relation_record_type"

    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,79}",
        }
    )
    direction: LdgroupDirectionType = field(
        default=LdgroupDirectionType.NON_DIRECTIONAL,
        metadata={
            "type": "Attribute",
        },
    )
    psi_override: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
            "tokens": True,
        },
    )
    factors: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
            "tokens": True,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LdgrpRecType:
    class Meta:
        name = "ldgrp_rec_type"

    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,40}",
        }
    )
    limit_state: Ldcomblimitstate = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LdposType:
    class Meta:
        name = "ldpos_type"

    position: LdposPosType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    shift_y: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        },
    )
    shift_z: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        },
    )
    reference_point: LdposRefType = field(
        default=LdposRefType.CENTER_OF_GRAVITY,
        metadata={
            "type": "Attribute",
        },
    )
    rectangle_position: RecPosType = field(
        default=RecPosType.CENTER_CENTER,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LoadCaseType:
    class Meta:
        name = "load_case_type"

    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,80}",
        }
    )
    type_value: LoadcasetypeType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    duration_class: Loadcasedurationtype = field(
        default=Loadcasedurationtype.PERMANENT,
        metadata={
            "type": "Attribute",
        },
    )
    position: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{1,79}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LoadSubgroup:
    class Meta:
        name = "load_subgroup"

    load_case: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t0: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t8: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ldcase_pile: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    final_cs: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,79}",
        }
    )
    master: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class MassConversionType:
    class Meta:
        name = "mass_conversion_type"

    conversion: list[MassConversionType.Conversion] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Conversion:
        factor: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 10.0,
            }
        )
        load_case: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class PeCaseType:
    class Meta:
        name = "pe_case_type"

    factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    phase: PePhaseType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    load_case: str | LcPtcType | LcPileType = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Plasticity3DRecord(Plasticity3DForceRecord):
    class Meta:
        name = "plasticity3d_record"

    moment_x_neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    moment_x_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    moment_y_neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    moment_y_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    moment_z_neg: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )
    moment_z_pos: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )


@dataclass(kw_only=True)
class PointType2D(PointType1D):
    class Meta:
        name = "point_type_2d"

    y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PshData:
    class Meta:
        name = "psh_data"

    diameter: PshDiameterValue = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    cd: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.02,
            "max_inclusive": 10.0,
        }
    )
    n_x_dir: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 2,
            "max_inclusive": 50,
        }
    )
    n_y_dir: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 2,
            "max_inclusive": 50,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PtcShapeType:
    class Meta:
        name = "ptc_shape_type"

    start_point: PtcShapeStart = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    intermediate_point: list[PtcShapeInner] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    end_point: PtcShapeEnd = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    top: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -10.0,
            "max_inclusive": 10.0,
        }
    )
    bottom: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -10.0,
            "max_inclusive": 10.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PtcStrandLibType:
    class Meta:
        name = "ptc_strand_lib_type"

    ptc_strand_data: PtcStrandLibType.PtcStrandData = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class PtcStrandData:
        f_pk: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1.0,
                "max_inclusive": 10000.0,
            }
        )
        f_p01k: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_inclusive": 1.0,
                "max_inclusive": 10000.0,
            },
        )
        a_p: float = field(
            metadata={
                "name": "A_p",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1.0,
                "max_inclusive": 10000.0,
            }
        )
        e_p: float = field(
            metadata={
                "name": "E_p",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1.0,
                "max_inclusive": 10000000.0,
            }
        )
        density: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 10000.0,
            }
        )
        relaxation_class: int = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1,
                "max_inclusive": 3,
            }
        )
        rho_1000: float = field(
            metadata={
                "name": "Rho_1000",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100.0,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class ReferencelistType:
    class Meta:
        name = "referencelist_type"

    ref: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RfWireType:
    class Meta:
        name = "rf_wire_type"

    diameter: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 0.1,
        }
    )
    reinforcing_material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    profile: WireProfileType = field(
        default=WireProfileType.RIBBED,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RfmaterialType:
    class Meta:
        name = "rfmaterial_type"

    reinforcing_steel: RfmaterialType.ReinforcingSteel = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r".{0,15}",
        }
    )
    standard: Standardtype = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    country: Eurocodetype = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class ReinforcingSteel:
        fyk: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 10000000000.0,
            }
        )
        es: float = field(
            metadata={
                "name": "Es",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 10000000000.0,
            }
        )
        epsilon_uk: float = field(
            metadata={
                "name": "Epsilon_uk",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 10000000000.0,
            }
        )
        epsilon_ud: float = field(
            metadata={
                "name": "Epsilon_ud",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 10000000000.0,
            }
        )
        k: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 1.0,
                "max_inclusive": 10000000000.0,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class SeismicLoadGroup:
    class Meta:
        name = "seismic_load_group"

    custom_table: None | SeismicLoadGroup.CustomTable = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load_case: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    safety_factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    user_defined_cases: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class CustomTable:
        record: list[SeismicLoadGroup.CustomTable.Record] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Record:
            s: MethodSs = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            data: MethodSeis | float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": -100000000000000.0,
                    "max_exclusive": 100000000000000.0,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )


@dataclass(kw_only=True)
class SimpleTrussCapacityType:
    class Meta:
        name = "simple_truss_capacity_type"

    limit_force: TrussLimitType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Sj1BarConnectionType:
    class Meta:
        name = "sj_1bar_connection_type"

    bar1: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    load_combination: list[Sj1BarConnectionType.LoadCombination] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )

    @dataclass(kw_only=True)
    class LoadCombination:
        bar1_forces: SjForceType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        guid: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            }
        )
        value_2nd_order_calculation: bool = field(
            default=False,
            metadata={
                "name": "_2nd_order_calculation",
                "type": "Attribute",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class Sj2BarsConnectionType:
    class Meta:
        name = "sj_2bars_connection_type"

    bar1: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    bar2: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    load_combination: list[Sj2BarsConnectionType.LoadCombination] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )

    @dataclass(kw_only=True)
    class LoadCombination:
        bar1_forces: SjForceType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        bar2_forces: SjForceType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        guid: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            }
        )
        value_2nd_order_calculation: bool = field(
            default=False,
            metadata={
                "name": "_2nd_order_calculation",
                "type": "Attribute",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class Sj3BarsConnectionType:
    class Meta:
        name = "sj_3bars_connection_type"

    bar1: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    bar2: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    bar3: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    load_combination: list[Sj3BarsConnectionType.LoadCombination] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )

    @dataclass(kw_only=True)
    class LoadCombination:
        bar1_forces: SjForceType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        bar2_forces: SjForceType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        bar3_forces: SjForceType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        guid: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            }
        )
        value_2nd_order_calculation: bool = field(
            default=False,
            metadata={
                "name": "_2nd_order_calculation",
                "type": "Attribute",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class SjDataType:
    class Meta:
        name = "sj_data_type"

    type_value: SjDatatypeNames = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    value: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[!-~]{1}[ -~]{0,49}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SlabStiffnessFactors:
    class Meta:
        name = "slab_stiffness_factors"

    factors: list[SlabStiffnessRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 10,
            "max_occurs": 10,
        },
    )


@dataclass(kw_only=True)
class SpecCsLoadCaseItem:
    class Meta:
        name = "spec_cs_load_case_item"

    type_value: LcFinalCs | str = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
            "pattern": r"cs.[1-9]{1}[0-9]{0,4}",
        }
    )
    gamma: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class StbarHaunchType:
    class Meta:
        name = "stbar_haunch_type"

    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    base_bar: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    at_start: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    at_top: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    d: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    l: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    h: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    tw: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    tf: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0001,
            "max_inclusive": 10.0,
        }
    )
    bf: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class StbarSiffenerType:
    class Meta:
        name = "stbar_siffener_type"

    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    base_bar: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    pos: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SteelPlData:
    class Meta:
        name = "steel_pl_data"

    elasto_plastic_behaviour_u: bool = field(
        metadata={
            "name": "elasto_plastic_behaviour_U",
            "type": "Attribute",
            "required": True,
        }
    )
    elasto_plastic_strain_limit_u: bool = field(
        metadata={
            "name": "elasto_plastic_strain_limit_U",
            "type": "Attribute",
            "required": True,
        }
    )
    elasto_plastic_strain_limit_option_u: float = field(
        metadata={
            "name": "elasto_plastic_strain_limit_option_U",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 50.0,
        }
    )
    elasto_plastic_transverse_shear_u: bool = field(
        default=False,
        metadata={
            "name": "elasto_plastic_transverse_shear_U",
            "type": "Attribute",
        },
    )
    elasto_plastic_transverse_shear_option_u: EptsoType = field(
        default=EptsoType.PARABOLIC,
        metadata={
            "name": "elasto_plastic_transverse_shear_option_U",
            "type": "Attribute",
        },
    )
    elasto_plastic_behaviour_sq: bool = field(
        metadata={
            "name": "elasto_plastic_behaviour_Sq",
            "type": "Attribute",
            "required": True,
        }
    )
    elasto_plastic_strain_limit_sq: bool = field(
        metadata={
            "name": "elasto_plastic_strain_limit_Sq",
            "type": "Attribute",
            "required": True,
        }
    )
    elasto_plastic_strain_limit_option_sq: float = field(
        metadata={
            "name": "elasto_plastic_strain_limit_option_Sq",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 50.0,
        }
    )
    elasto_plastic_transverse_shear_sq: bool = field(
        default=False,
        metadata={
            "name": "elasto_plastic_transverse_shear_Sq",
            "type": "Attribute",
        },
    )
    elasto_plastic_transverse_shear_option_sq: EptsoType = field(
        default=EptsoType.PARABOLIC,
        metadata={
            "name": "elasto_plastic_transverse_shear_option_Sq",
            "type": "Attribute",
        },
    )
    elasto_plastic_behaviour_sf: bool = field(
        metadata={
            "name": "elasto_plastic_behaviour_Sf",
            "type": "Attribute",
            "required": True,
        }
    )
    elasto_plastic_strain_limit_sf: bool = field(
        metadata={
            "name": "elasto_plastic_strain_limit_Sf",
            "type": "Attribute",
            "required": True,
        }
    )
    elasto_plastic_strain_limit_option_sf: float = field(
        metadata={
            "name": "elasto_plastic_strain_limit_option_Sf",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 50.0,
        }
    )
    elasto_plastic_transverse_shear_sf: bool = field(
        default=False,
        metadata={
            "name": "elasto_plastic_transverse_shear_Sf",
            "type": "Attribute",
        },
    )
    elasto_plastic_transverse_shear_option_sf: EptsoType = field(
        default=EptsoType.PARABOLIC,
        metadata={
            "name": "elasto_plastic_transverse_shear_option_Sf",
            "type": "Attribute",
        },
    )
    elasto_plastic_behaviour_sc: bool = field(
        metadata={
            "name": "elasto_plastic_behaviour_Sc",
            "type": "Attribute",
            "required": True,
        }
    )
    elasto_plastic_strain_limit_sc: bool = field(
        metadata={
            "name": "elasto_plastic_strain_limit_Sc",
            "type": "Attribute",
            "required": True,
        }
    )
    elasto_plastic_strain_limit_option_sc: float = field(
        metadata={
            "name": "elasto_plastic_strain_limit_option_Sc",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 50.0,
        }
    )
    elasto_plastic_transverse_shear_sc: bool = field(
        default=False,
        metadata={
            "name": "elasto_plastic_transverse_shear_Sc",
            "type": "Attribute",
        },
    )
    elasto_plastic_transverse_shear_option_sc: EptsoType = field(
        default=EptsoType.PARABOLIC,
        metadata={
            "name": "elasto_plastic_transverse_shear_option_Sc",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class StiffBaseType:
    class Meta:
        name = "stiff_base_type"

    neg: float | StiffnessMaxReached = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    pos: float | StiffnessMaxReached = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class StiffnessMotionRecord:
    class Meta:
        name = "stiffness_motion_record"

    kx_neg: float | StiffnessMaxReached = field(
        metadata={
            "name": "Kx_neg",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    kx_pos: float | StiffnessMaxReached = field(
        metadata={
            "name": "Kx_pos",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    ky_neg: float | StiffnessMaxReached = field(
        metadata={
            "name": "Ky_neg",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    ky_pos: float | StiffnessMaxReached = field(
        metadata={
            "name": "Ky_pos",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    kz_neg: float | StiffnessMaxReached = field(
        metadata={
            "name": "Kz_neg",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    kz_pos: float | StiffnessMaxReached = field(
        metadata={
            "name": "Kz_pos",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class StiffnessType:
    class Meta:
        name = "stiffness_type"

    x_neg: float | StiffnessMaxReached = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    x_pos: float | StiffnessMaxReached = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    y_neg: float | StiffnessMaxReached = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    y_pos: float | StiffnessMaxReached = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    z_neg: float | StiffnessMaxReached = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    z_pos: float | StiffnessMaxReached = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TdaCreep1:
    class Meta:
        name = "tda_creep1"

    creep_compliance_prony_series: None | TdaCreepProny = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    creep_compliance_by_data_set: None | TdaCreepComplianceGeneral = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class TdaCreepEn1992:
    class Meta:
        name = "tda_creep_EN1992"

    t0: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100000000.0,
        }
    )
    rh: float = field(
        metadata={
            "name": "RH",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    calculate_ac_u: bool = field(
        metadata={
            "name": "calculate_Ac_u",
            "type": "Attribute",
            "required": True,
        }
    )
    ac: float = field(
        metadata={
            "name": "Ac",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1.798e38,
        }
    )
    u: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1.798e38,
        }
    )
    sigma_relevant: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    cement_type: CementType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    increase_final_value: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TdaElasticity:
    class Meta:
        name = "tda_elasticity"

    general: None | TdaElasticity.General = field(
        default=None,
        metadata={
            "name": "General",
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    en_1992_1_1_2004: None | TdaElasticity.En1992112004 = field(
        default=None,
        metadata={
            "name": "EN_1992-1-1_2004",
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )

    @dataclass(kw_only=True)
    class General:
        record: list[TdaElasticity.General.Record] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Record:
            t: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 0.0,
                    "max_inclusive": 100000000.0,
                }
            )
            e: float = field(
                metadata={
                    "name": "E",
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": 0.0,
                    "max_inclusive": 100000000.0,
                }
            )

    @dataclass(kw_only=True)
    class En1992112004:
        cement_type: CementType = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        t0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000000.0,
            }
        )


@dataclass(kw_only=True)
class TdaShrinkage:
    class Meta:
        name = "tda_shrinkage"

    general: None | TdaShrinkage.General = field(
        default=None,
        metadata={
            "name": "General",
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    en_1992_1_1_2004: None | TdaShrinkage.En1992112004 = field(
        default=None,
        metadata={
            "name": "EN_1992-1-1_2004",
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )

    @dataclass(kw_only=True)
    class General:
        record: list[TdaShrinkage.General.Record] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )

        @dataclass(kw_only=True)
        class Record:
            t: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 0.0,
                    "max_inclusive": 100000000.0,
                }
            )
            strain: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 0.0,
                    "max_inclusive": 100000000.0,
                }
            )

    @dataclass(kw_only=True)
    class En1992112004:
        ts: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000000.0,
            }
        )
        rh: float = field(
            metadata={
                "name": "RH",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100.0,
            }
        )
        calculate_ac_u: bool = field(
            metadata={
                "name": "calculate_Ac_u",
                "type": "Attribute",
                "required": True,
            }
        )
        ac: float = field(
            metadata={
                "name": "Ac",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 1.798e38,
            }
        )
        u: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 1.798e38,
            }
        )
        cement_type: CementType = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class TpDatatype:
    class Meta:
        name = "tp_datatype"

    stiffness: TpDatatype.Stiffness = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    strength: TpDatatype.Strength = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    service_class_0_factors: ServiceClassFactors = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    service_class_1_factors: ServiceClassFactors = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    service_class_2_factors: ServiceClassFactors = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    description: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,40}",
        }
    )
    thickness: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 100.0,
        }
    )
    gamma_m_u: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        },
    )
    gamma_m_as: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        },
    )
    service_class: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 2,
        },
    )
    system_factor: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Stiffness:
        em_k0: float = field(
            metadata={
                "name": "Em_k0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        em_k90: float = field(
            metadata={
                "name": "Em_k90",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        et_k0: float = field(
            metadata={
                "name": "Et_k0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        et_k90: float = field(
            metadata={
                "name": "Et_k90",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        ec_k0: float = field(
            metadata={
                "name": "Ec_k0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        ec_k90: float = field(
            metadata={
                "name": "Ec_k90",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        gr_k0: float = field(
            metadata={
                "name": "Gr_k0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        gr_k90: float = field(
            metadata={
                "name": "Gr_k90",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        gv_k: float = field(
            metadata={
                "name": "Gv_k",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        rho: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Strength:
        fm_k0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        fm_k90: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        ft_k0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        ft_k90: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        fc_k0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        fc_k90: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        fr_k0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        fr_k90: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        fv_k: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 100000.0,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class TrussCapacityType:
    class Meta:
        name = "truss_capacity_type"

    limit_force: list[TrussLimitType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 9,
            "max_occurs": 9,
        },
    )


@dataclass(kw_only=True)
class TsContourlineType:
    class Meta:
        name = "ts_contourline_type"

    vertex: list[TsIndexedVertexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 3,
            "max_occurs": 32767,
        },
    )


@dataclass(kw_only=True)
class TsVisibleEdgeType:
    class Meta:
        name = "ts_visible_edge_type"

    vertex: list[TsIndexedVertexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 32767,
        },
    )
    linetype: Visiblelinetype = field(
        default=Visiblelinetype.LINE,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class UniqueSpectraType:
    class Meta:
        name = "unique_spectra_type"

    record: list[SpectraRecordType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 127,
        },
    )
    start_sd: float = field(
        metadata={
            "name": "start_Sd",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EcG2SeismicLoadType:
    class Meta:
        name = "EC_G2_seismic_load_type"

    standard_spectrum: None | EcG2SeismicLoadType.StandardSpectrum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    unique_spectrum: None | EcG2SeismicLoadType.UniqueSpectrum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bridge_pier: list[BridgePierType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    structure_type: SeismicStructureType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    xi: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    q_r: float = field(
        metadata={
            "name": "qR",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    q_s: float = field(
        metadata={
            "name": "qS",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    q_d: float = field(
        metadata={
            "name": "qD",
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    qv: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    qdisp: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class StandardSpectrum:
        horizontal: EcG2HorizontalSpectraType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        vertical: EcG2VerticalSpectraType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class UniqueSpectrum:
        horizontal: EcG2UniqueSpectraType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        vertical: EcG2UniqueSpectraType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class AxisLabelProps:
    class Meta:
        name = "axis_label_props"

    font: FontType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colour: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Fa-f]{6}",
        }
    )
    penwidth: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BoltLibType:
    class Meta:
        name = "bolt_lib_type"

    bolt_data: BoltDataType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CltpanelLibType:
    class Meta:
        name = "cltpanel_lib_type"

    clt_panel_data: CltDatatype = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CompositeData:
    class Meta:
        name = "composite_data"

    part: list[CompositePartType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 8,
        },
    )
    property: list[CompositePropType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 11,
        },
    )
    type_value: CompositeType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ConcretePlData:
    class Meta:
        name = "concrete_pl_data"

    u: ConcretePlAttribs = field(
        metadata={
            "name": "U",
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    sq: ConcretePlAttribs = field(
        metadata={
            "name": "Sq",
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    sf: ConcretePlAttribs = field(
        metadata={
            "name": "Sf",
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    sc: ConcretePlAttribs = field(
        metadata={
            "name": "Sc",
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CsStageType:
    class Meta:
        name = "cs_stage_type"

    activated_load_case: list[CsLcType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    description: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,79}",
        }
    )
    initial_stress_state: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    day: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e20,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EccentricityType:
    class Meta:
        name = "eccentricity_type"

    analytical: list[EccValueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    physical: list[EccValueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    use_default_physical_alignment: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EfCombinationType:
    class Meta:
        name = "ef_combination_type"

    record: list[EfLcaseRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    dt: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class GlcpanelLibType:
    class Meta:
        name = "glcpanel_lib_type"

    glc_panel_data: GlcDatatype = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class GroundAccelerationType:
    class Meta:
        name = "ground_acceleration_type"

    diagram: list[GaDiagramType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    combination: list[GaCombinationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class HorizontalPolygon2D:
    class Meta:
        name = "horizontal_polygon_2d"

    point: list[PointType2D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 3,
        },
    )
    height: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class LdgroupRelationTable:
    class Meta:
        name = "ldgroup_relation_table"

    record: list[LdgroupRelationRecordType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class LdgrpCtType:
    class Meta:
        name = "ldgrp_ct_type"

    record: list[LdgrpRecType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class LoadCombinationType:
    class Meta:
        name = "load_combination_type"

    load_case: list[LoadCombinationType.LoadCase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    seismic_max: None | SpecLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    seismic_res_fx_plus_mx: None | SpecLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    seismic_res_fx_minus_mx: None | SpecLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    seismic_res_fy_plus_my: None | SpecLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    seismic_res_fy_minus_my: None | SpecLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    seismic_res_fz: None | SpecLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t0: None | SpecLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t8: None | SpecLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ldcase_pile: None | SpecLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    cs_case: None | SpecCsLoadCaseItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,159}",
        }
    )
    type_value: Loadcombtype = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class LoadCase:
        guid: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            }
        )
        gamma: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class PanelConnectionsType:
    class Meta:
        name = "panel_connections_type"

    bottom_edge: ConnSideType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    right_edge: ConnSideType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    top_edge: ConnSideType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    left_edge: ConnSideType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    internal_edges: ConnSideType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PeRecordType:
    class Meta:
        name = "pe_record_type"

    case: list[PeCaseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    frequency: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PileRigidityGroupType:
    class Meta:
        name = "pile_rigidity_group_type"

    springs: list[StiffnessMotionRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 10,
            "max_occurs": 10,
        },
    )
    plastic_limits: list[Plasticity3DForceRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 10,
            "max_occurs": 10,
        },
    )


@dataclass(kw_only=True)
class PileRigidityGroupType1:
    class Meta:
        name = "pile_rigidity_group_type1"

    spring: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plastic_limit_forces: PlasticityType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PileRigidityGroupType2:
    class Meta:
        name = "pile_rigidity_group_type2"

    spring: list[StiffBaseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 10,
            "max_occurs": 10,
        },
    )
    plastic_limit_forces: list[PlasticityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 10,
            "max_occurs": 10,
        },
    )


@dataclass(kw_only=True)
class PointType3D(PointType2D):
    class Meta:
        name = "point_type_3d"

    z: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class RigidityDataType0:
    class Meta:
        name = "rigidity_data_type0"

    motions: StiffnessType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plastic_limit_forces: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    detach: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    wx: float = field(
        default=0.0,
        metadata={
            "name": "Wx",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )


@dataclass(kw_only=True)
class RigidityGroupType0:
    class Meta:
        name = "rigidity_group_type0"

    springs: list[StiffnessMotionRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 10,
            "max_occurs": 10,
        },
    )
    plastic_limits: list[Plasticity3DForceRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 4,
            "max_occurs": 4,
        },
    )
    wx: float = field(
        default=0.0,
        metadata={
            "name": "Wx",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )


@dataclass(kw_only=True)
class SeismicLoadType:
    class Meta:
        name = "seismic_load_type"

    common_standard_spectra: None | SeismicLoadType.CommonStandardSpectra = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    ec040_standard_spectra: None | SeismicLoadType.Ec040StandardSpectra = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    unique_spectra: None | SeismicLoadType.UniqueSpectra = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    xi: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 50.0,
        }
    )
    qd: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    building_structure: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    gamma_ie: float = field(
        default=1.0,
        metadata={
            "name": "Gamma_Ie",
            "type": "Attribute",
            "min_inclusive": 0.5,
            "max_inclusive": 10.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class CommonStandardSpectra:
        horizontal: StandardSpectraType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        vertical: StandardSpectraType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        ground: SeismicGroundType = field(
            default=SeismicGroundType.A,
            metadata={
                "type": "Attribute",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Ec040StandardSpectra:
        horizontal: Ec040StandardSpectraType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class UniqueSpectra:
        horizontal: UniqueSpectraType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        vertical: UniqueSpectraType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class SimpleRigidityGroup:
    class Meta:
        name = "simple_rigidity_group"

    springs: list[StiffBaseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 10,
            "max_occurs": 10,
        },
    )
    plastic_limits: list[PlasticityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 4,
            "max_occurs": 4,
        },
    )
    plastic_limits2: list[PlasticityType2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 6,
            "max_occurs": 6,
        },
    )
    type_value: MotionType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SimpleRigidityType:
    class Meta:
        name = "simple_rigidity_type"

    mov: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    rot: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plastic_limit_forces: None | PlasticityType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic_limit_moments: None | PlasticityType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class SimpleSpringType:
    class Meta:
        name = "simple_spring_type"

    mov_x: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    rot_x: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    mov_y: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    rot_y: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    mov_z: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    rot_z: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    detach: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SimpleStiffnessType:
    class Meta:
        name = "simple_stiffness_type"

    mov_x: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    rot_x: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    mov_y: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    rot_y: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    mov_z: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    rot_z: StiffBaseType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    detach: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SimpleTrussBehaviourType:
    class Meta:
        name = "simple_truss_behaviour_type"

    elastic: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    brittle: None | SimpleTrussCapacityType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic: None | SimpleTrussCapacityType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class SjComponentType:
    class Meta:
        name = "sj_component_type"

    record: SjComponentType.Record = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    bolt_rows: None | SjComponentType.BoltRows = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    type_value: SjComponentValues = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    connected_to: SjConnectedBarType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Record:
        property: list[SjDataType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
                "max_occurs": 17,
            },
        )

    @dataclass(kw_only=True)
    class BoltRows:
        row: list[SjBoltlineType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class StiffnessRecord(StiffnessMotionRecord):
    class Meta:
        name = "stiffness_record"

    cx_neg: float | StiffnessMaxReached = field(
        metadata={
            "name": "Cx_neg",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    cx_pos: float | StiffnessMaxReached = field(
        metadata={
            "name": "Cx_pos",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    cy_neg: float | StiffnessMaxReached = field(
        metadata={
            "name": "Cy_neg",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    cy_pos: float | StiffnessMaxReached = field(
        metadata={
            "name": "Cy_pos",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    cz_neg: float | StiffnessMaxReached = field(
        metadata={
            "name": "Cz_neg",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    cz_pos: float | StiffnessMaxReached = field(
        metadata={
            "name": "Cz_pos",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        }
    )
    wx: float = field(
        default=0.0,
        metadata={
            "name": "Wx",
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1000000000000000.0,
        },
    )


@dataclass(kw_only=True)
class TdaCreep2:
    class Meta:
        name = "tda_creep2"

    creep_compliance_prony_series: None | TdaCreepProny = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    en_1992_1_1_2004: None | TdaCreepEn1992 = field(
        default=None,
        metadata={
            "name": "EN_1992-1-1_2004",
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    creep_compliance_by_data_set: None | TdaCreepComplianceGeneral = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class TextFontType(FontType):
    class Meta:
        name = "text_font_type"

    h_align: HorAlign = field(
        default=HorAlign.LEFT,
        metadata={
            "type": "Attribute",
        },
    )
    v_align: VerAlign = field(
        default=VerAlign.BOTTOM,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class TimberpanelLibType:
    class Meta:
        name = "timberpanel_lib_type"

    timber_panel_data: TpDatatype = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TrussBehaviourType:
    class Meta:
        name = "truss_behaviour_type"

    elastic: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    brittle: None | TrussCapacityType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic: None | TrussCapacityType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class TrussEccentricityType:
    class Meta:
        name = "truss_eccentricity_type"

    physical: list[EccValueType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    use_default_physical_alignment: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TsContourType:
    class Meta:
        name = "ts_contour_type"

    contour: list[TsContourlineType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 32767,
        },
    )


@dataclass(kw_only=True)
class WallConnectionsType:
    class Meta:
        name = "wall_connections_type"

    bottom_edge: ConnSideType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    right_edge: ConnSideType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    top_edge: ConnSideType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    left_edge: ConnSideType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class AccidentalLoadGroup:
    class Meta:
        name = "accidental_load_group"

    custom_table: None | AccidentalLoadGroup.CustomTable = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load_case: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t0: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t8: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ldcase_pile: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    final_cs: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    subgroup: list[LoadSubgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    relations: None | LdgroupRelationTable = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    safety_factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    using_psi_1: bool = field(
        default=True,
        metadata={
            "name": "using_Psi_1",
            "type": "Attribute",
        },
    )
    snow_effect: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    relationship: LdgroupRelation = field(
        default=LdgroupRelation.ALTERNATIVE,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class CustomTable:
        record: list[AccidentalLoadGroup.CustomTable.Record] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Record:
            s: MethodSs = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            data: MethodAcc | float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": -100000000000000.0,
                    "max_exclusive": 100000000000000.0,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )


@dataclass(kw_only=True)
class AxisType:
    class Meta:
        name = "axis_type"

    start_point: PointType2D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    end_point: PointType2D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    label_props: None | AxisLabelProps = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    prefix: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r".{0,15}",
        },
    )
    has_prefix: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    id: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 321272406,
        }
    )
    id_is_letter: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    priority: PriorityType = field(
        default=PriorityType.PRIMARY,
        metadata={
            "type": "Attribute",
        },
    )
    use_for_views: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    label_position: AxisPosition = field(
        default=AxisPosition.START,
        metadata={
            "type": "Attribute",
        },
    )
    distance_from_end_point: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BeamReductionZoneType:
    class Meta:
        name = "beam_reduction_zone_type"

    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    extent_definition: None | BeamEdType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    base_beam: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    moment_reduction_method: MrmType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    automatic_extent_definition: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    moment_reduction: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    shear_reduction: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    connected_to: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BucklingRecord:
    class Meta:
        name = "buckling_record"

    start_point: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    end_point: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    position: None | SegmentpositionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    type_value: BarBucklingType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    beta: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
        },
    )
    continously_restrained: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    cantilever: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    load_position: VerAlign = field(
        default=VerAlign.TOP,
        metadata={
            "type": "Attribute",
        },
    )
    sway: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ComplexSectionType:
    class Meta:
        name = "complex_section_type"

    section: list[ComplexSectionType.Section] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Section:
        ecc: None | PointType3D = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        ecc_phys: None | PointType3D = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        end: EmptyType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        any_element: list[object] = field(
            default_factory=list,
            metadata={
                "type": "Wildcard",
                "namespace": "##any",
            },
        )
        guid: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            },
        )
        pos: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 1.0,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class CsType:
    class Meta:
        name = "cs_type"

    stage: list[CsStageType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 32768,
        },
    )
    auto_assign_modified_elements: bool = field(
        default=False,
        metadata={
            "name": "auto-assign_modified_elements",
            "type": "Attribute",
        },
    )
    auto_assign_newly_created_elements: bool = field(
        default=False,
        metadata={
            "name": "auto-assign_newly_created_elements",
            "type": "Attribute",
        },
    )
    ghost_method: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    time_dependent_analysis: bool = field(
        default=False,
        metadata={
            "name": "time-dependent_analysis",
            "type": "Attribute",
        },
    )
    creep_strain_increment_limit: float = field(
        default=0.25,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DimtextType:
    class Meta:
        name = "dimtext_type"

    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plane_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plane_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    value: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    text: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        },
    )
    decimals: int = field(
        default=2,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 10,
        },
    )
    length_unit: LengthunitType = field(
        default=LengthunitType.M,
        metadata={
            "type": "Attribute",
        },
    )
    angle_unit: AngleunitType = field(
        default=AngleunitType.RAD,
        metadata={
            "type": "Attribute",
        },
    )
    measurement_unit: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    prefix: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,15}",
        },
    )
    suffix: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,15}",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    h_align: HalignType = field(
        default=HalignType.CENTERED,
        metadata={
            "type": "Attribute",
        },
    )
    v_align: ValignType = field(
        default=ValignType.ABOVE,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ExcavationType:
    class Meta:
        name = "excavation_type"

    contour: HorizontalPolygon2D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    depth: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ExcitationForceType:
    class Meta:
        name = "excitation_force_type"

    diagram: list[EfDiagramType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    combination: list[EfCombinationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class Fdarc3Type:
    class Meta:
        name = "fdarc3_type"

    centre: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    radius: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e23,
        }
    )
    start_angle: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 6.28318530717959,
        }
    )
    end_angle: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 6.28318530717959,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class FillingType:
    class Meta:
        name = "filling_type"

    contour: HorizontalPolygon2D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    level_point: list[LevelPointType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    default_top_level: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    default_bottom_level: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -100000.0,
            "max_inclusive": 100000.0,
        }
    )
    material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    colour: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9A-Fa-f]{6}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class GenStjointType:
    class Meta:
        name = "gen_stjoint_type"

    connection_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    connected_items: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            "tokens": True,
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LabsecgeomType:
    class Meta:
        name = "labsecgeom_type"

    line_segment: None | LabsecgeomType.LineSegment = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    polyline: None | LabsecgeomType.Polyline = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="A",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class LineSegment:
        start_point: PointType3D = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        base_point: PointType3D = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        end_point: PointType3D = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        reverse_direction: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Polyline:
        point: list[PointType3D] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 3,
            },
        )


@dataclass(kw_only=True)
class LineType:
    class Meta:
        name = "line_type"

    start: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    end: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocalsysType:
    class Meta:
        name = "localsys_type"

    centre: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class LocationValue(PointType3D):
    class Meta:
        name = "location_value"

    val: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )


@dataclass(kw_only=True)
class MassPointType:
    class Meta:
        name = "mass_point_type"

    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    value: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1e-15,
            "max_inclusive": 1e20,
        },
    )
    apply_on_ecc: None | bool = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    comment: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class MaterialType:
    class Meta:
        name = "material_type"

    concrete: None | MaterialType.Concrete = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    steel: None | MaterialType.Steel = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    timber: None | MaterialType.Timber = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    brick: None | MaterialType.Brick = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    masonry: None | MaterialType.Masonry = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    stratum: None | MaterialType.Stratum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    custom: None | MaterialType.Custom = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    reference: None | ReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,256}",
        }
    )
    standard: Standardtype = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    country: Eurocodetype = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Concrete:
        tda_creep: None | TdaCreep2 = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        tda_shrinkage: None | TdaShrinkage = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        tda_elasticity: None | TdaElasticity = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        plastic_analysis_data: None | ConcretePlData = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        mass: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 1e20,
            }
        )
        e_0: float = field(
            metadata={
                "name": "E_0",
                "type": "Attribute",
                "required": True,
            }
        )
        e_1: float = field(
            metadata={
                "name": "E_1",
                "type": "Attribute",
                "required": True,
            }
        )
        e_2: float = field(
            metadata={
                "name": "E_2",
                "type": "Attribute",
                "required": True,
            }
        )
        nu_0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        nu_1: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        nu_2: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_1: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_2: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        g_0: float = field(
            metadata={
                "name": "G_0",
                "type": "Attribute",
                "required": True,
            }
        )
        g_1: float = field(
            metadata={
                "name": "G_1",
                "type": "Attribute",
                "required": True,
            }
        )
        g_2: float = field(
            metadata={
                "name": "G_2",
                "type": "Attribute",
                "required": True,
            }
        )
        fck: float = field(
            metadata={
                "name": "Fck",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fck_cube: float = field(
            default=30.0,
            metadata={
                "name": "Fck_cube",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        fctk: float = field(
            metadata={
                "name": "Fctk",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fctm: float = field(
            metadata={
                "name": "Fctm",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        ecm: float = field(
            metadata={
                "name": "Ecm",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_c_0: None | float = field(
            default=None,
            metadata={
                "name": "gammaC_0",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_c_1: None | float = field(
            default=None,
            metadata={
                "name": "gammaC_1",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_ce: float = field(
            metadata={
                "name": "gammaCE",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_ce_1: float = field(
            default=1.15,
            metadata={
                "name": "gammaCE_1",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_cfi: float = field(
            default=1.0,
            metadata={
                "name": "gammaCfi",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_s_0: float = field(
            metadata={
                "name": "gammaS_0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_s_1: float = field(
            metadata={
                "name": "gammaS_1",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_sfi: float = field(
            default=1.0,
            metadata={
                "name": "gammaSfi",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        alfa_cc: None | float = field(
            default=None,
            metadata={
                "name": "alfaCc",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        alfa_ct: None | float = field(
            default=None,
            metadata={
                "name": "alfaCt",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        fcd_0: float = field(
            metadata={
                "name": "Fcd_0",
                "type": "Attribute",
                "required": True,
            }
        )
        fcd_1: float = field(
            metadata={
                "name": "Fcd_1",
                "type": "Attribute",
                "required": True,
            }
        )
        fctd_0: float = field(
            metadata={
                "name": "Fctd_0",
                "type": "Attribute",
                "required": True,
            }
        )
        fctd_1: float = field(
            metadata={
                "name": "Fctd_1",
                "type": "Attribute",
                "required": True,
            }
        )
        ecd_0: float = field(
            metadata={
                "name": "Ecd_0",
                "type": "Attribute",
                "required": True,
            }
        )
        ecd_1: float = field(
            metadata={
                "name": "Ecd_1",
                "type": "Attribute",
                "required": True,
            }
        )
        epsc2: None | float = field(
            default=None,
            metadata={
                "name": "Epsc2",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        epscu2: None | float = field(
            default=None,
            metadata={
                "name": "Epscu2",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        epsc3: None | float = field(
            default=None,
            metadata={
                "name": "Epsc3",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        epscu3: None | float = field(
            default=None,
            metadata={
                "name": "Epscu3",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        environment: None | int = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        creep: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        creep_sls: float = field(
            default=0.0,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        creep_slf: float = field(
            default=0.0,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        creep_slc: float = field(
            default=0.0,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        shrinkage: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 1000.0,
            }
        )
        nu: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 0.499,
            }
        )
        alfa: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        reduction: float = field(
            default=1.0,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_inclusive": 10.0,
            },
        )
        stability: float = field(
            default=1.0,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_inclusive": 1.0,
            },
        )
        ktc: float = field(
            default=1.0,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        ktt: float = field(
            default=1.0,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        epscu: float = field(
            default=0.0035,
            metadata={
                "name": "Epscu",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_v_0: float = field(
            default=1.0,
            metadata={
                "name": "gammaV_0",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_v_1: float = field(
            default=1.0,
            metadata={
                "name": "gammaV_1",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_v_fi: float = field(
            default=1.0,
            metadata={
                "name": "gammaV_fi",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        d_lower: float = field(
            default=8.0,
            metadata={
                "name": "D_lower",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Steel:
        tda_creep: None | TdaCreep1 = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        plastic_analysis_data: None | SteelPlData = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        mass: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 1e20,
            }
        )
        e_0: float = field(
            metadata={
                "name": "E_0",
                "type": "Attribute",
                "required": True,
            }
        )
        e_1: float = field(
            metadata={
                "name": "E_1",
                "type": "Attribute",
                "required": True,
            }
        )
        e_2: float = field(
            metadata={
                "name": "E_2",
                "type": "Attribute",
                "required": True,
            }
        )
        nu_0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        nu_1: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        nu_2: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_1: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_2: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        g_0: float = field(
            metadata={
                "name": "G_0",
                "type": "Attribute",
                "required": True,
            }
        )
        g_1: float = field(
            metadata={
                "name": "G_1",
                "type": "Attribute",
                "required": True,
            }
        )
        g_2: float = field(
            metadata={
                "name": "G_2",
                "type": "Attribute",
                "required": True,
            }
        )
        fyk16: float = field(
            metadata={
                "name": "Fyk16",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fyk40: float = field(
            metadata={
                "name": "Fyk40",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fyk63: float = field(
            metadata={
                "name": "Fyk63",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fyk80: float = field(
            metadata={
                "name": "Fyk80",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fyk100: float = field(
            metadata={
                "name": "Fyk100",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fyk150: float = field(
            metadata={
                "name": "Fyk150",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fyk200: float = field(
            metadata={
                "name": "Fyk200",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fyk250: float = field(
            metadata={
                "name": "Fyk250",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fyk400: float = field(
            metadata={
                "name": "Fyk400",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fuk3: float = field(
            metadata={
                "name": "Fuk3",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fuk40: float = field(
            metadata={
                "name": "Fuk40",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fuk100: float = field(
            metadata={
                "name": "Fuk100",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fuk150: float = field(
            metadata={
                "name": "Fuk150",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fuk250: float = field(
            metadata={
                "name": "Fuk250",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fuk400: float = field(
            metadata={
                "name": "Fuk400",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m0_0: float = field(
            metadata={
                "name": "gammaM0_0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m0_1: float = field(
            metadata={
                "name": "gammaM0_1",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m1_0: float = field(
            metadata={
                "name": "gammaM1_0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m1_1: float = field(
            metadata={
                "name": "gammaM1_1",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m2_0: float = field(
            metadata={
                "name": "gammaM2_0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m2_1: float = field(
            metadata={
                "name": "gammaM2_1",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m5_0: None | float = field(
            default=None,
            metadata={
                "name": "gammaM5_0",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_m5_1: None | float = field(
            default=None,
            metadata={
                "name": "gammaM5_1",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_mfi: float = field(
            default=1.0,
            metadata={
                "name": "gammaMfi",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        ek: float = field(
            metadata={
                "name": "Ek",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        ed_0: float = field(
            metadata={
                "name": "Ed_0",
                "type": "Attribute",
                "required": True,
            }
        )
        ed_1: float = field(
            metadata={
                "name": "Ed_1",
                "type": "Attribute",
                "required": True,
            }
        )
        nu: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 0.499,
            }
        )
        g: float = field(
            metadata={
                "name": "G",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        alfa: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Timber:
        tda_creep: None | TdaCreep1 = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        mass: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 1e20,
            }
        )
        e_0: float = field(
            metadata={
                "name": "E_0",
                "type": "Attribute",
                "required": True,
            }
        )
        e_1: float = field(
            metadata={
                "name": "E_1",
                "type": "Attribute",
                "required": True,
            }
        )
        e_2: float = field(
            metadata={
                "name": "E_2",
                "type": "Attribute",
                "required": True,
            }
        )
        nu_0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        nu_1: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        nu_2: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_1: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_2: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        g_0: float = field(
            metadata={
                "name": "G_0",
                "type": "Attribute",
                "required": True,
            }
        )
        g_1: float = field(
            metadata={
                "name": "G_1",
                "type": "Attribute",
                "required": True,
            }
        )
        g_2: float = field(
            metadata={
                "name": "G_2",
                "type": "Attribute",
                "required": True,
            }
        )
        type_value: int = field(
            metadata={
                "name": "type",
                "type": "Attribute",
                "required": True,
            }
        )
        quality: int = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        fmk0: float = field(
            metadata={
                "name": "Fmk0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fmk90: float = field(
            metadata={
                "name": "Fmk90",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        ft0k: float = field(
            metadata={
                "name": "Ft0k",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        ft90k: float = field(
            metadata={
                "name": "Ft90k",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fc0k: float = field(
            metadata={
                "name": "Fc0k",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fc90k: float = field(
            metadata={
                "name": "Fc90k",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fvk: float = field(
            metadata={
                "name": "Fvk",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        e0mean: float = field(
            metadata={
                "name": "E0mean",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        e90mean: float = field(
            metadata={
                "name": "E90mean",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        e005: float = field(
            metadata={
                "name": "E005",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gmean: float = field(
            metadata={
                "name": "Gmean",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        g005: float = field(
            metadata={
                "name": "G005",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        rhok: float = field(
            metadata={
                "name": "Rhok",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        rhomean: float = field(
            metadata={
                "name": "Rhomean",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        e0comp: float = field(
            metadata={
                "name": "E0comp",
                "type": "Attribute",
                "required": True,
            }
        )
        e90comp: float = field(
            metadata={
                "name": "E90comp",
                "type": "Attribute",
                "required": True,
            }
        )
        gamma_m_0: float = field(
            metadata={
                "name": "gammaM_0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m_1: float = field(
            metadata={
                "name": "gammaM_1",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        ksys: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        k_cr: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_inclusive": 1.0,
            },
        )
        service_class: int = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0,
                "max_inclusive": 2,
            }
        )
        kdef_u: None | float = field(
            default=None,
            metadata={
                "name": "kdefU",
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        kdef_sq: None | float = field(
            default=None,
            metadata={
                "name": "kdefSq",
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        kdef_sf: None | float = field(
            default=None,
            metadata={
                "name": "kdefSf",
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        kdef_sc: None | float = field(
            default=None,
            metadata={
                "name": "kdefSc",
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        gamma_mfi: None | float = field(
            default=None,
            metadata={
                "name": "gammaMfi",
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Brick:
        base_data: None | OptionalMaterialAttribs = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        strength_for: StrengthType = field(
            default=StrengthType.BRICK_ONLY,
            metadata={
                "type": "Attribute",
            },
        )
        fb: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        nu: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 0.499,
            }
        )
        rho: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        alpha_thermal: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m_0: float = field(
            metadata={
                "name": "gammaM_0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m_1: float = field(
            metadata={
                "name": "gammaM_1",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fm: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        k: float = field(
            metadata={
                "name": "K",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        alpha: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        beta: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        elasticity_modulus: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        elasticity_calculated_by_ke: bool = field(
            default=False,
            metadata={
                "name": "elasticity_calculated_by_KE",
                "type": "Attribute",
            },
        )
        creep_u: float = field(
            metadata={
                "name": "creep_U",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        creep_sq: float = field(
            metadata={
                "name": "creep_Sq",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        creep_sf: float = field(
            metadata={
                "name": "creep_Sf",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        creep_sc: float = field(
            metadata={
                "name": "creep_Sc",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        phi: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        filled_vertical_joints: None | bool = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        km: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        muk: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        ct: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        fvk0: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        fvlt: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        muf: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_inclusive": 1.0,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Masonry:
        base_data: None | OptionalMaterialAttribs = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        strength_for: StrengthType = field(
            default=StrengthType.BRICK_ONLY,
            metadata={
                "type": "Attribute",
            },
        )
        fk: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        nu: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 0.499,
            }
        )
        rho: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        alpha_thermal: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m_0: float = field(
            metadata={
                "name": "gammaM_0",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_m_1: float = field(
            metadata={
                "name": "gammaM_1",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        fm: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        k: float = field(
            metadata={
                "name": "K",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        alpha: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        beta: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        elasticity_modulus: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        elasticity_calculated_by_ke: bool = field(
            default=False,
            metadata={
                "name": "elasticity_calculated_by_KE",
                "type": "Attribute",
            },
        )
        creep_u: float = field(
            metadata={
                "name": "creep_U",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        creep_sq: float = field(
            metadata={
                "name": "creep_Sq",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        creep_sf: float = field(
            metadata={
                "name": "creep_Sf",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        creep_sc: float = field(
            metadata={
                "name": "creep_Sc",
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        phi: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        filled_vertical_joints: None | bool = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        km: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        muk: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        ct: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        fvk0: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        fvlt: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Stratum:
        base_data: None | OptionalMaterialAttribs = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        behaviour: MaterialType.Stratum.Behaviour = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        model: MaterialType.Stratum.Model = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        reference_level: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        gamma_dry: float = field(
            metadata={
                "name": "Gamma_dry",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        gamma_sat: float = field(
            metadata={
                "name": "Gamma_sat",
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_exclusive": 3.403e38,
            }
        )
        nu: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 0.499,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

        @dataclass(kw_only=True)
        class Behaviour:
            drained: None | MaterialType.Stratum.Behaviour.Drained = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                },
            )
            undrained: None | MaterialType.Stratum.Behaviour.Undrained = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                },
            )
            combined: None | MaterialType.Stratum.Behaviour.Combined = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                },
            )

            @dataclass(kw_only=True)
            class Drained:
                c_k: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                c_k_depth: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                phi_k: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_inclusive": 1.5690509975429,
                    }
                )
                phi_cvk: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_inclusive": 1.5690509975429,
                    }
                )

            @dataclass(kw_only=True)
            class Undrained:
                c_uk: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                c_uk_depth: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )

            @dataclass(kw_only=True)
            class Combined:
                drained: bool = field(
                    default=False,
                    metadata={
                        "type": "Attribute",
                    },
                )
                c_uk: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                c_uk_depth: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                c_k: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                c_k_depth: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                phi_k: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_inclusive": 1.5690509975429,
                    }
                )
                phi_cvk: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_inclusive": 1.5690509975429,
                    }
                )

        @dataclass(kw_only=True)
        class Model:
            generic: None | MaterialType.Stratum.Model.Generic = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                },
            )
            linear: None | MaterialType.Stratum.Model.Linear = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                },
            )
            overconsolidated: (
                None | MaterialType.Stratum.Model.Overconsolidated
            ) = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                },
            )

            @dataclass(kw_only=True)
            class Generic:
                record: list[MaterialType.Stratum.Model.Generic.Record] = (
                    field(
                        default_factory=list,
                        metadata={
                            "type": "Element",
                            "namespace": "urn:strusoft",
                            "min_occurs": 1,
                            "max_occurs": 5,
                        },
                    )
                )
                mu: float = field(
                    metadata={
                        "name": "Mu",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                mu_depth: float = field(
                    metadata={
                        "name": "Mu_depth",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )

                @dataclass(kw_only=True)
                class Record:
                    sigma: float = field(
                        metadata={
                            "name": "Sigma",
                            "type": "Attribute",
                            "required": True,
                            "min_exclusive": 0.0,
                            "max_inclusive": 100000.0,
                        }
                    )
                    p: float = field(
                        metadata={
                            "type": "Attribute",
                            "required": True,
                            "min_inclusive": 0.0,
                            "max_inclusive": 100000.0,
                        }
                    )
                    pd: float = field(
                        metadata={
                            "type": "Attribute",
                            "required": True,
                            "min_inclusive": 0.0,
                            "max_inclusive": 100000.0,
                        }
                    )
                    m: float = field(
                        metadata={
                            "name": "M",
                            "type": "Attribute",
                            "required": True,
                            "min_exclusive": 0.0,
                            "max_inclusive": 100000.0,
                        }
                    )
                    md: float = field(
                        metadata={
                            "name": "Md",
                            "type": "Attribute",
                            "required": True,
                            "min_inclusive": 0.0,
                            "max_inclusive": 100000.0,
                        }
                    )

            @dataclass(kw_only=True)
            class Linear:
                use_e: bool = field(
                    default=False,
                    metadata={
                        "name": "use_E",
                        "type": "Attribute",
                    },
                )
                value: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                m0_depth: float = field(
                    metadata={
                        "name": "M0_depth",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )

            @dataclass(kw_only=True)
            class Overconsolidated:
                mu: float = field(
                    metadata={
                        "name": "Mu",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                mu_depth: float = field(
                    metadata={
                        "name": "Mu_depth",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                m0: float = field(
                    metadata={
                        "name": "M0",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                m0_depth: float = field(
                    metadata={
                        "name": "M0_depth",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                ml: float = field(
                    metadata={
                        "name": "ML",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                ml_depth: float = field(
                    metadata={
                        "name": "ML_depth",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                m: float = field(
                    metadata={
                        "name": "M",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                m_depth: float = field(
                    metadata={
                        "name": "M_depth",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                sigma_c: float = field(
                    metadata={
                        "name": "Sigma_c",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                p_c: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                pc_depth: float = field(
                    metadata={
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                sigma_l: float = field(
                    metadata={
                        "name": "Sigma_L",
                        "type": "Attribute",
                        "required": True,
                        "min_exclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                p_l: float = field(
                    metadata={
                        "name": "p_L",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )
                p_l_depth: float = field(
                    metadata={
                        "name": "p_L_depth",
                        "type": "Attribute",
                        "required": True,
                        "min_inclusive": 0.0,
                        "max_exclusive": 3.403e38,
                    }
                )

    @dataclass(kw_only=True)
    class Custom:
        mass: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_inclusive": 0.0,
                "max_inclusive": 1e20,
            }
        )
        e_0: float = field(
            metadata={
                "name": "E_0",
                "type": "Attribute",
                "required": True,
            }
        )
        e_1: float = field(
            metadata={
                "name": "E_1",
                "type": "Attribute",
                "required": True,
            }
        )
        e_2: float = field(
            metadata={
                "name": "E_2",
                "type": "Attribute",
                "required": True,
            }
        )
        nu_0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        nu_1: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        nu_2: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_0: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_1: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        alfa_2: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        g_0: float = field(
            metadata={
                "name": "G_0",
                "type": "Attribute",
                "required": True,
            }
        )
        g_1: float = field(
            metadata={
                "name": "G_1",
                "type": "Attribute",
                "required": True,
            }
        )
        g_2: float = field(
            metadata={
                "name": "G_2",
                "type": "Attribute",
                "required": True,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class OptLocalsysType:
    class Meta:
        name = "opt_localsys_type"

    local_pos: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class PeriodicExcitationType:
    class Meta:
        name = "periodic_excitation_type"

    record: list[PeRecordType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PermanentLoadGroup:
    class Meta:
        name = "permanent_load_group"

    custom_table: None | PermanentLoadGroup.CustomTable = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load_case: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t0: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t8: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ldcase_pile: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    final_cs: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    subgroup: list[LoadSubgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    relations: None | LdgroupRelationTable = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    standard_favourable: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    standard_unfavourable: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    accidental_favourable: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    accidental_unfavourable: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    xi: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    relationship: LdgroupRelation = field(
        default=LdgroupRelation.ALTERNATIVE,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class CustomTable:
        record: list[PermanentLoadGroup.CustomTable.Record] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Record:
            s: MethodSs = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            data: MethodPer | float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": -100000000000000.0,
                    "max_exclusive": 100000000000000.0,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )


@dataclass(kw_only=True)
class PtcType:
    class Meta:
        name = "ptc_type"

    start_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    end_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_z: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    losses: PtcLosses = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    shape_base_points: PtcShapeType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    manufacturing: PtcManufacturingType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    base_object: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    name: str = field(
        default="PTC",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    strand_type: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    number_of_strands: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 100,
        }
    )
    jacking_side: PtcJackingSide = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    jacking_stress: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 200.0,
            "max_inclusive": 10000000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RectangleType:
    class Meta:
        name = "rectangle_type"

    base_corner: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    x_direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    y_direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    x_size: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10000.0,
        }
    )
    y_size: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10000.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ReslineType:
    class Meta:
        name = "resline_type"

    start: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    end: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    y_axis: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    base_entity: list[RlBaseType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="VB",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RespointType:
    class Meta:
        name = "respoint_type"

    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    font: None | FontType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="PT",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    base_entity: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RigidityDataType1(RigidityDataType0):
    class Meta:
        name = "rigidity_data_type1"

    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RigidityGroupType1(RigidityGroupType0):
    class Meta:
        name = "rigidity_group_type1"

    detach: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RigidityGroupType2:
    class Meta:
        name = "rigidity_group_type2"

    springs: list[StiffnessRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 10,
            "max_occurs": 10,
        },
    )
    plastic_limits: list[Plasticity3DRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 4,
            "max_occurs": 4,
        },
    )
    detach: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ShellRfParamsType:
    class Meta:
        name = "shell_rf_params_type"

    base_shell: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    center: ShellRfParamsType.Center = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    x_direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    y_direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    single_layer_reinforcement: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Center:
        x: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        y: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        z: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        polar_system: bool = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class SimpleTrussChrType:
    class Meta:
        name = "simple_truss_chr_type"

    compression: SimpleTrussBehaviourType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    tension: SimpleTrussBehaviourType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class SjTopologyType:
    class Meta:
        name = "sj_topology_type"

    component: list[SjComponentType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 16,
        },
    )


@dataclass(kw_only=True)
class StiffnessPointType:
    class Meta:
        name = "stiffness_point_type"

    rigidity: None | RigidityDataType0 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType0 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    surface_support: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    z: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class StiffnessWithFriction(SimpleStiffnessType):
    class Meta:
        name = "stiffness_with_friction"

    friction: float = field(
        default=0.3,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )


@dataclass(kw_only=True)
class StoreyType:
    class Meta:
        name = "storey_type"

    origo: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType2D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    dimension_x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
        }
    )
    dimension_y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{0,256}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class StrataType:
    class Meta:
        name = "strata_type"

    contour: HorizontalPolygon2D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    stratum: list[StratumType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )
    water_level: list[WaterLevelType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    default_filling: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    default_fillings_colour: str = field(
        default="B97A57",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    depth_level_limit: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000000.0,
            "max_exclusive": 0.0,
        }
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class StressLoadGroup:
    class Meta:
        name = "stress_load_group"

    custom_table: None | StressLoadGroup.CustomTable = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load_case: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t0: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t8: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ldcase_pile: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    final_cs: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    subgroup: list[LoadSubgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    relations: None | LdgroupRelationTable = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    standard: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    accidental: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    relationship: LdgroupRelation = field(
        default=LdgroupRelation.ALTERNATIVE,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class CustomTable:
        record: list[StressLoadGroup.CustomTable.Record] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Record:
            s: MethodSs = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            data: MethodStr | float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": -100000000000000.0,
                    "max_exclusive": 100000000000000.0,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )


@dataclass(kw_only=True)
class StyleType:
    class Meta:
        name = "style_type"

    filling: None | FillType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    font: None | TextFontType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    layer: str = field(
        default="0",
        metadata={
            "type": "Attribute",
            "pattern": r"[\t\n\r -�]{1,255}",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    line_style: InternalLineStyle | str = field(
        default=InternalLineStyle.CONTINUOUS,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        },
    )
    penwidth: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -10000.0,
            "max_inclusive": 10000.0,
        },
    )
    point_style: PointstyleType = field(
        default=PointstyleType.CROSS,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SurfaceRfLineType:
    class Meta:
        name = "surface_rf_line_type"

    start_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    end_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    wire: RfWireType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    base_shell: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    side: SfRcFace = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    right_side_wires: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    pieces: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 100,
        }
    )
    space: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0001,
            "max_inclusive": 10.0,
        }
    )
    cover: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    colour: str = field(
        default="0000a0",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TemporaryLoadGroup:
    class Meta:
        name = "temporary_load_group"

    custom_table: None | TemporaryLoadGroup.CustomTable = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load_case: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t0: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ptc_t8: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ldcase_pile: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    final_cs: None | EmptyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load_cases_of_moving_load: list[
        TemporaryLoadGroup.LoadCasesOfMovingLoad
    ] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    subgroup: list[LoadSubgroup] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    relations: None | LdgroupRelationTable = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    safety_factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    psi_0: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    psi_1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    psi_2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    leading_cases: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    ignore_sls: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    simultaneous: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    relationship: LdgroupRelation = field(
        default=LdgroupRelation.ALTERNATIVE,
        metadata={
            "type": "Attribute",
        },
    )
    temporary_effect: LdgroupTmpeffect = field(
        default=LdgroupTmpeffect.GENERAL,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class CustomTable:
        record: list[TemporaryLoadGroup.CustomTable.Record] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
            },
        )

        @dataclass(kw_only=True)
        class Record:
            s: MethodSs = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            data: MethodTmp | float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": -100000000000000.0,
                    "max_exclusive": 100000000000000.0,
                }
            )
            i: MethodIs = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )

    @dataclass(kw_only=True)
    class LoadCasesOfMovingLoad:
        guid: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            }
        )
        master: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class TopbottomValue(PointType3D):
    class Meta:
        name = "topbottom_value"

    top_val: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )
    bottom_val: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )


@dataclass(kw_only=True)
class TrussChrType:
    class Meta:
        name = "truss_chr_type"

    compression: TrussBehaviourType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    tension: TrussBehaviourType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class TsSurfaceType:
    class Meta:
        name = "ts_surface_type"

    flat_face: list[TsContourType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 32767,
        },
    )


@dataclass(kw_only=True)
class TsVertexType:
    class Meta:
        name = "ts_vertex_type"

    vertex: list[PointType3D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 4,
            "max_occurs": 32767,
        },
    )


@dataclass(kw_only=True)
class UntestedLocalsysType:
    class Meta:
        name = "untested_localsys_type"

    pos: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    z: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class WbrType:
    class Meta:
        name = "wbr_type"

    connected_wall: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    pt: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    dir: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    stirrup_pt: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    stirrup_dir: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ApexBucklingType:
    class Meta:
        name = "apex_buckling_type"

    buckling_length: list[BucklingRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class BucklingDataType:
    class Meta:
        name = "buckling_data_type"

    buckling_length: list[BucklingRecord] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class BuildingCoverType:
    class Meta:
        name = "building_cover_type"

    base_rectangle: RectangleType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    supporting_structures: None | ReferencelistType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    covers: None | CoverlistType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    roof_type: RoofType = field(
        default=RoofType.FLAT,
        metadata={
            "type": "Attribute",
        },
    )
    h_wall: float = field(
        default=6.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 10000.0,
        },
    )
    h_roof: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CaselessPointLoadType:
    class Meta:
        name = "caseless_point_load_type"

    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    load: LocationValue = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    load_position: None | LdposType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_type: ForceLoadType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    apply_on_ecc: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_dir: None | DirectionType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_sign: None | AutoForceSignType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_type: None | AutoForceTypeType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    assigned_structure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )


@dataclass(kw_only=True)
class DimangleType:
    class Meta:
        name = "dimangle_type"

    arc: Fdarc3Type = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    base: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    line1: LineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    line2: LineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    dimension_line: DimdimlineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    extension_line: ExtlineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    arrow: ArrowType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    font: FontType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    text: DimtextType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    beta: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    rs1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    re1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    rs2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    re2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    layer: str = field(
        default="DIM",
        metadata={
            "type": "Attribute",
            "pattern": r"[\t\n\r -�]{1,255}",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DimarcType:
    class Meta:
        name = "dimarc_type"

    arc: Fdarc3Type = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    dimension_line: DimdimlineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    extension_line: ExtlineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    arrow: ArrowType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    font: FontType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    text: DimtextType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    layer: str = field(
        default="DIM",
        metadata={
            "type": "Attribute",
            "pattern": r"[\t\n\r -�]{1,255}",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DimdiamType:
    class Meta:
        name = "dimdiam_type"

    arc: Fdarc3Type = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    dimension_line: DimdimlineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    arrow: ArrowType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    font: FontType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    text: DimtextType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    layer: str = field(
        default="DIM",
        metadata={
            "type": "Attribute",
            "pattern": r"[\t\n\r -�]{1,255}",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DimfloorType:
    class Meta:
        name = "dimfloor_type"

    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plane_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plane_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    font: FontType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    text: DimtextType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    size: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e23,
        }
    )
    layer: str = field(
        default="DIM",
        metadata={
            "type": "Attribute",
            "pattern": r"[\t\n\r -�]{1,255}",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DimlineType:
    class Meta:
        name = "dimline_type"

    point: list[PointType3D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
        },
    )
    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plane_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plane_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    dimension_line: DimdimlineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    extension_line: ExtlineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    arrow: ArrowType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    font: FontType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    text: list[DimtextType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    dynamic: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    layer: str = field(
        default="DIM",
        metadata={
            "type": "Attribute",
            "pattern": r"[\t\n\r -�]{1,255}",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DimradiusType:
    class Meta:
        name = "dimradius_type"

    arc: Fdarc3Type = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    dimension_line: DimdimlineType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    arrow: ArrowType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    font: FontType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    text: DimtextType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    layer: str = field(
        default="DIM",
        metadata={
            "type": "Attribute",
            "pattern": r"[\t\n\r -�]{1,255}",
        },
    )
    colour: str = field(
        default="000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class GeneralLoadGroupType:
    class Meta:
        name = "general_load_group_type"

    accidental: None | AccidentalLoadGroup = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    permanent: None | PermanentLoadGroup = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    seismic: None | SeismicLoadGroup = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    stress: None | StressLoadGroup = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    temporary: None | TemporaryLoadGroup = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,79}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    consider_in_gmax: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PointSupportLoadType:
    class Meta:
        name = "point_support_load_type"

    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    displacement: LocationValue = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    load_type: MotionType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PointType:
    class Meta:
        name = "point_type"

    location: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    style: None | StyleType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class PolyhedronType:
    class Meta:
        name = "polyhedron_type"

    vertices_in_index_order: TsVertexType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    visible_edge: list[TsVisibleEdgeType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 32767,
        },
    )
    surface: list[TsSurfaceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 32767,
        },
    )
    fillmode: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    fillcolor: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RigidityDataType2(RigidityDataType1):
    class Meta:
        name = "rigidity_data_type2"

    rotations: StiffnessType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    plastic_limit_moments: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class RigidityDatalibType1:
    class Meta:
        name = "rigidity_datalib_type1"

    rigidity: None | RigidityDataType1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RigidityGroupType3(RigidityGroupType2):
    class Meta:
        name = "rigidity_group_type3"

    friction: float = field(
        default=0.3,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )


@dataclass(kw_only=True)
class SteelJointType:
    class Meta:
        name = "steel_joint_type"

    column_splice_solution1: None | SteelJointType.ColumnSpliceSolution1 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    column_splice_solution2: None | SteelJointType.ColumnSpliceSolution2 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    column_splice_solution3: None | SteelJointType.ColumnSpliceSolution3 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    column_splice_solution4: None | SteelJointType.ColumnSpliceSolution4 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    column_splice_solution5: None | SteelJointType.ColumnSpliceSolution5 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    column_splice_solution6: None | SteelJointType.ColumnSpliceSolution6 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    beam_splice_solution1: None | SteelJointType.BeamSpliceSolution1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_splice_solution2: None | SteelJointType.BeamSpliceSolution2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_splice_solution3: None | SteelJointType.BeamSpliceSolution3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_splice_solution4: None | SteelJointType.BeamSpliceSolution4 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_splice_solution5: None | SteelJointType.BeamSpliceSolution5 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_splice_solution6: None | SteelJointType.BeamSpliceSolution6 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_splice_solution7: None | SteelJointType.BeamSpliceSolution7 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    column_base_solution1: None | SteelJointType.ColumnBaseSolution1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    column_base_solution2: None | SteelJointType.ColumnBaseSolution2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_to_beam_solution1: None | SteelJointType.BeamToBeamSolution1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_to_beam_solution2: None | SteelJointType.BeamToBeamSolution2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_to_beam_solution3: None | SteelJointType.BeamToBeamSolution3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_to_beam_solution4: None | SteelJointType.BeamToBeamSolution4 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_to_beam_solution5: None | SteelJointType.BeamToBeamSolution5 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    beam_to_column_solution1: None | SteelJointType.BeamToColumnSolution1 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    beam_to_column_solution2: None | SteelJointType.BeamToColumnSolution2 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    beam_to_column_solution3: None | SteelJointType.BeamToColumnSolution3 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    beam_to_column_solution4: None | SteelJointType.BeamToColumnSolution4 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    beam_to_column_solution5a: None | SteelJointType.BeamToColumnSolution5A = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    beam_to_column_solution5b: None | SteelJointType.BeamToColumnSolution5B = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    beam_to_column_solution6: None | SteelJointType.BeamToColumnSolution6 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    beam_to_column_solution7: None | SteelJointType.BeamToColumnSolution7 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    beam_to_column_solution8: None | SteelJointType.BeamToColumnSolution8 = (
        field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
    )
    knee_solution1: None | SteelJointType.KneeSolution1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    knee_solution2: None | SteelJointType.KneeSolution2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    knee_solution3: None | SteelJointType.KneeSolution3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    knee_solution4: None | SteelJointType.KneeSolution4 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    knee_solution5a: None | SteelJointType.KneeSolution5A = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    knee_solution5b: None | SteelJointType.KneeSolution5B = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    knee_solution6a: None | SteelJointType.KneeSolution6A = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    knee_solution6b: None | SteelJointType.KneeSolution6B = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    knee_solution7: None | SteelJointType.KneeSolution7 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    knee_solution8: None | SteelJointType.KneeSolution8 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution1y: None | SteelJointType.BracingSolution1Y = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution1x: None | SteelJointType.BracingSolution1X = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution1k: None | SteelJointType.BracingSolution1K = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution2y: None | SteelJointType.BracingSolution2Y = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution2x: None | SteelJointType.BracingSolution2X = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution2k: None | SteelJointType.BracingSolution2K = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution3y: None | SteelJointType.BracingSolution3Y = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution3x: None | SteelJointType.BracingSolution3X = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution3k: None | SteelJointType.BracingSolution3K = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution4: None | SteelJointType.BracingSolution4 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution5: None | SteelJointType.BracingSolution5 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    bracing_solution6: None | SteelJointType.BracingSolution6 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    topology: None | SjTopologyType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="SJ",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    version: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class ColumnSpliceSolution1:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ColumnSpliceSolution2:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ColumnSpliceSolution3:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ColumnSpliceSolution4:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ColumnSpliceSolution5:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ColumnSpliceSolution6:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamSpliceSolution1:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamSpliceSolution2:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamSpliceSolution3:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamSpliceSolution4:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamSpliceSolution5:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamSpliceSolution6:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamSpliceSolution7:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ColumnBaseSolution1:
        connecting_bars: Sj1BarConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class ColumnBaseSolution2:
        connecting_bars: Sj1BarConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToBeamSolution1:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToBeamSolution2:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToBeamSolution3:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToBeamSolution4:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToBeamSolution5:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToColumnSolution1:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToColumnSolution2:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToColumnSolution3:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToColumnSolution4:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToColumnSolution5A:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToColumnSolution5B:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToColumnSolution6:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToColumnSolution7:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BeamToColumnSolution8:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution1:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution2:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution3:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution4:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution5A:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution5B:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution6A:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution6B:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution7:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class KneeSolution8:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution1Y:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution1X:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution1K:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution2Y:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution2X:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution2K:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution3Y:
        connecting_bars: Sj2BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution3X:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution3K:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution4:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution5:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class BracingSolution6:
        connecting_bars: Sj3BarsConnectionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )


@dataclass(kw_only=True)
class SurfaceRfRectType:
    class Meta:
        name = "surface_rf_rect_type"

    wire: RfWireType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    rectangle: RectangleType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    base_shell: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    side: SfRcFace = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    pieces: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 100,
        }
    )
    cover: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e17,
        }
    )
    colour: str = field(
        default="0000a0",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class TextType:
    class Meta:
        name = "text_type"

    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    style: StyleType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    text: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[\t\n\r -�]{0,1023}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ViewType1:
    class Meta:
        name = "view_type"

    coordinate_system_2d: UntestedLocalsysType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    coordinate_system_3d: UntestedLocalsysType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    user_coordinate_system: UntestedLocalsysType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    scale: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_exclusive": 3.403e38,
        }
    )
    tolerance: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_exclusive": 3.403e38,
        }
    )
    type_value: Viewtype2 = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ApexType:
    class Meta:
        name = "apex_type"

    center: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    intersection_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    buckling_data: list[ApexBucklingType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    r: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 100.0,
        }
    )
    rounded_edge: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ConnectedPointsType:
    class Meta:
        name = "connected_points_type"

    point: list[PointType3D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    stiffness: None | SimpleStiffnessType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic_limit_forces: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic_limit_moments: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity: None | RigidityDataType2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    predefined_rigidity: None | ReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ref: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="CP",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    interface: float = field(
        default=0.5,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class HiddenBarType:
    class Meta:
        name = "hidden_bar_type"

    rectangle: RectangleType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    start: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    buckling_data: None | BucklingDataType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    end: EmptyType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    base_shell: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    axis_in_longer_side: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LoadGroupTable:
    class Meta:
        name = "load_group_table"

    custom_table: None | LdgrpCtType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    group: list[GeneralLoadGroupType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    simple_combination_method: Ldcombmethod = field(
        default=Ldcombmethod.EN_1990_6_4_3_6_10,
        metadata={
            "type": "Attribute",
        },
    )
    k_f: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 10.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PointLoadType(CaselessPointLoadType):
    class Meta:
        name = "point_load_type"

    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RigidityDataType3(RigidityDataType2):
    class Meta:
        name = "rigidity_data_type3"

    friction: float = field(
        default=0.3,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )


@dataclass(kw_only=True)
class RigidityDatalibType2:
    class Meta:
        name = "rigidity_datalib_type2"

    rigidity: None | RigidityDataType2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType2 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SupportRigidityDataType:
    class Meta:
        name = "support_rigidity_data_type"

    directed: None | SupportRigidityDataType.Directed = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    group: None | SupportRigidityDataType.Group = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    warping: None | SupportRigidityDataType.Warping = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )

    @dataclass(kw_only=True)
    class Directed:
        direction: PointType3D = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        mov: None | StiffBaseType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        rot: None | StiffBaseType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        plastic_limit_forces: None | PlasticityType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        plastic_limit_moments: None | PlasticityType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        rigidity_group: None | SimpleRigidityGroup = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )

    @dataclass(kw_only=True)
    class Group:
        local_x: PointType3D = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        local_y: PointType3D = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        mov_x: None | StiffBaseType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        rot_x: None | StiffBaseType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        mov_y: None | StiffBaseType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        rot_y: None | StiffBaseType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        mov_z: None | StiffBaseType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        rot_z: None | StiffBaseType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        plastic_limit_forces: None | PlasticityType3D = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        plastic_limit_moments: None | PlasticityType3D = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        rigidity: None | RigidityDataType2 = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        predefined_rigidity: None | ReferenceType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        rigidity_group: None | RigidityGroupType2 = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        detach: str = field(
            default="",
            metadata={
                "type": "Attribute",
            },
        )
        seven_degrees_of_freedom: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Warping:
        wx: list[float] = field(
            default_factory=list,
            metadata={
                "name": "Wx",
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_inclusive": 1000000000000000.0,
                "tokens": True,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class EcType:
    class Meta:
        name = "ec_type"

    stiffness: None | StiffnessWithFriction = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic_limit_forces: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic_limit_moments: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity: None | RigidityDataType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    predefined_rigidity: None | ReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="CE",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    moving_local: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    joined_start_point: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    joined_end_point: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PointSupportType(SupportRigidityDataType):
    class Meta:
        name = "point_support_type"

    position: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="S",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RigidityDatalibType3:
    class Meta:
        name = "rigidity_datalib_type3"

    rigidity: None | RigidityDataType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class WallCorbelType:
    class Meta:
        name = "wall_corbel_type"

    start_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    end_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    connectable_parts: None | TwoGuidListType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity: None | RigidityDataType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    predefined_rigidity: None | ReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    positive_side: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    l: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    h1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    h2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 10.0,
        }
    )
    base_wall: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    complex_material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EcEdgeListItemType:
    class Meta:
        name = "ec_edge_list_item_type"

    edge_connection: EcType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    edge_index: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class EdgeType1:
    class Meta:
        name = "edge_type"

    point: list[PointType3D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    normal: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    x_axis: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    edge_connection: None | EcType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    physical_extent: None | PheType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    reinforcement_anchorage: None | AncType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    type_value: Edgetype2 = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    radius: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 1000.0,
        },
    )
    start_angle: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    end_angle: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BarPartType:
    class Meta:
        name = "bar_part_type"

    curve: EdgeType1 = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "name": "local-y",
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    connectivity: list[ConnectivityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 2,
        },
    )
    eccentricity: None | EccentricityType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    buckling_data: None | BucklingDataType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    camber_simulation: None | CamberType2D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    stiffness_modifiers: None | BarStiffnessFactors = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    end: EmptyType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    complex_material: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    complex_section: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    complex_composite: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    made: Steelmadetype = field(
        default=Steelmadetype.ROLLED,
        metadata={
            "type": "Attribute",
        },
    )
    ecc_mode: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    ecc_calc: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    ecc_crack: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    first_order_analysis_u: bool = field(
        default=False,
        metadata={
            "name": "first_order_analysis_U",
            "type": "Attribute",
        },
    )
    first_order_analysis_sq: bool = field(
        default=False,
        metadata={
            "name": "first_order_analysis_Sq",
            "type": "Attribute",
        },
    )
    first_order_analysis_sf: bool = field(
        default=False,
        metadata={
            "name": "first_order_analysis_Sf",
            "type": "Attribute",
        },
    )
    first_order_analysis_sc: bool = field(
        default=False,
        metadata={
            "name": "first_order_analysis_Sc",
            "type": "Attribute",
        },
    )
    seven_degrees_of_freedom: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class CaselessLineLoadResultantType:
    class Meta:
        name = "caseless_line_load_resultant_type"

    edge: EdgeType1 = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    normal: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load: list[LocationValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 2,
        },
    )
    resultant: None | ResultantType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load_position: None | LdposType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_type: ForceLoadType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    apply_on_ecc: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_dir: None | DirectionType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_sign: None | AutoForceSignType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_type: None | AutoForceTypeType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    assigned_structure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    load_dir: LoadDirType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    load_projection: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CaselessLineLoadType:
    class Meta:
        name = "caseless_line_load_type"

    edge: EdgeType1 = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    normal: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load: list[LocationValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    load_position: None | LdposType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_type: ForceLoadType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    apply_on_ecc: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_dir: None | DirectionType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_sign: None | AutoForceSignType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_type: None | AutoForceTypeType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    assigned_structure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    load_dir: LoadDirType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    load_projection: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class ConnectedLinesType:
    class Meta:
        name = "connected_lines_type"

    edge: list[EdgeType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    point: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    stiffness: None | SimpleStiffnessType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic_limit_forces: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic_limit_moments: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity: None | RigidityDataType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    predefined_rigidity: None | ReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ref: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="CL",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    moving_local: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    interface_start: float = field(
        default=0.5,
        metadata={
            "type": "Attribute",
        },
    )
    interface_end: float = field(
        default=0.5,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ContourType:
    class Meta:
        name = "contour_type"

    edge: list[EdgeType1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CoverReferencelistType:
    class Meta:
        name = "cover_referencelist_type"

    ref: list[CoverReferencelistType.Ref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Ref:
        edge: list[EdgeType1] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        guid: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class CurveType(EdgeType1):
    class Meta:
        name = "curve_type"

    style: None | StyleType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class LineStressLoadType:
    class Meta:
        name = "line_stress_load_type"

    edge: EdgeType1 = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    normal: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    stress: list[TopbottomValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LineSupportLoadType:
    class Meta:
        name = "line_support_load_type"

    edge: EdgeType1 = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    normal: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    displacement: list[LocationValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    load_type: MotionType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    load_dir: LoadDirType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LineSupportType(SupportRigidityDataType):
    class Meta:
        name = "line_support_type"

    edge: EdgeType1 = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    normal: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="S",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    moving_local: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LineTemperatureLoadType:
    class Meta:
        name = "line_temperature_load_type"

    edge: EdgeType1 = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    normal: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    temperature: list[TopbottomValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PilesBeamType:
    class Meta:
        name = "piles_beam_type"

    curve: EdgeType1 = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "name": "local-y",
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    connectivity: ConnectivityType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    buckling_data: None | BucklingDataType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    complex_material: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    complex_section: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    complex_composite: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    made: Steelmadetype = field(
        default=Steelmadetype.ROLLED,
        metadata={
            "type": "Attribute",
        },
    )
    guid: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class VirtualBarType:
    class Meta:
        name = "virtual_bar_type"

    edge: EdgeType1 = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "name": "local-y",
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    connectivity: list[ConnectivityType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 2,
        },
    )
    truss_behaviour: None | SimpleTrussChrType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="BF",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    ae: float = field(
        metadata={
            "name": "AE",
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1e-05,
            "max_inclusive": 1000000000000000.0,
        }
    )
    unit_mass: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000000.0,
        },
    )
    it_g: float = field(
        default=10000000.0,
        metadata={
            "name": "ItG",
            "type": "Attribute",
            "min_inclusive": 1e-05,
            "max_inclusive": 1000000000000000.0,
        },
    )
    i1_e: float = field(
        default=10000000.0,
        metadata={
            "name": "I1E",
            "type": "Attribute",
            "min_inclusive": 1e-05,
            "max_inclusive": 1000000000000000.0,
        },
    )
    i2_e: float = field(
        default=10000000.0,
        metadata={
            "name": "I2E",
            "type": "Attribute",
            "min_inclusive": 1e-05,
            "max_inclusive": 1000000000000000.0,
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BarType:
    class Meta:
        name = "bar_type"

    bar_part: list[BarPartType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    apex: list[ApexType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    truss_behaviour: None | TrussChrType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    eccentricity: None | TrussEccentricityType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    end: EmptyType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    type_value: Beamtype = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    shell_model: ShellModelType = field(
        default=ShellModelType.NONE,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    maxforce: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e30,
        },
    )
    compressions_plasticity: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    tension: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e30,
        },
    )
    tensions_plasticity: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DrawingRegionType:
    class Meta:
        name = "drawing_region_type"

    contour: list[ContourType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    style: None | StyleType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LineLoadType(CaselessLineLoadResultantType):
    class Meta:
        name = "line_load_type"

    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class LnfoundationType:
    class Meta:
        name = "lnfoundation_type"

    bar_part: BarPartType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    referable_parts: None | LnfoundationRefType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    insulation: None | FoundationInsulationType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="F",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    bedding_modulus: float = field(
        default=10000.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 100000000.0,
        },
    )
    analythical_system: FoundationsystemsType = field(
        default=FoundationsystemsType.SIMPLE,
        metadata={
            "type": "Attribute",
        },
    )
    fillmode: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    fillcolor: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class MovingLoadGridType:
    class Meta:
        name = "moving_load_grid_type"

    local_pos: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    contour: list[ContourType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    grid_x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 1000.0,
        }
    )
    grid_y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 1000.0,
        }
    )
    edge_x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )
    edge_y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        }
    )


@dataclass(kw_only=True)
class NoshearRegionType:
    class Meta:
        name = "noshear_region_type"

    automatic: None | NoshearAutoType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    contour: None | ContourType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    base_plate: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PileType:
    class Meta:
        name = "pile_type"

    beam: PilesBeamType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    point_support: None | PileType.PointSupport = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    line_support: list[PileType.LineSupport] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="PI",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    type_value: PiletypeType = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    division_length: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.1,
            "max_inclusive": 100.0,
        }
    )
    surface_surcharge: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    neutral_level: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1000.0,
        }
    )
    auto_calculate: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    perimeter_by_contour: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class PointSupport:
        rigidity: None | PileRigidityGroupType1 = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        rigidity_group: None | PileRigidityGroupType2 = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        guid: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class LineSupport:
        rigidity: None | RigidityDataType0 = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        rigidity_group: None | PileRigidityGroupType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        alpha_neg: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        beta_neg: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        guid: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class PsrType:
    class Meta:
        name = "psr_type"

    contour: list[ContourType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    inactive: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RegionType:
    class Meta:
        name = "region_type"

    contour: list[ContourType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class ShearControlRegionType:
    class Meta:
        name = "shear_control_region_type"

    automatic: None | ShearControlAutoType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    contour: list[ContourType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    base_plate: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    ignore_shear_check: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 20.0,
        }
    )
    physical_extension: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.01,
            "max_inclusive": 100.0,
        },
    )
    reduce_shear_forces: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ShellBucklingType:
    class Meta:
        name = "shell_buckling_type"

    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    contour: ContourType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    base_shell: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    beta: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SlabPartType:
    class Meta:
        name = "slab_part_type"

    contour: list[ContourType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    thickness: list[LocationValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    local_pos: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    stiffness_modifiers: None | SlabStiffnessFactors = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    connections: None | WallConnectionsType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    end: EmptyType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    complex_material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    alignment: VerAlign = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    align_offset: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        },
    )
    ortho_alfa: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 3.14159265358979,
        },
    )
    ortho_ratio: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    ecc_calc: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    ecc_crack: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    refracting_angle: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.5707963267949,
        },
    )
    mesh_size: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e20,
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    application_of_geometric_changes: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class BarRfType:
    class Meta:
        name = "bar_rf_type"

    base_bar: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    wire: RfWireType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    stirrups: None | BarRfType.Stirrups = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    longitudinal_bar: None | BarRfType.LongitudinalBar = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Stirrups:
        region: RegionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        start: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        end: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        distance: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class LongitudinalBar:
        cross_sectional_position: PointType2D = field(
            metadata={
                "name": "cross-sectional_position",
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        anchorage: StartEndType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        prescribed_lengthening: None | StartEndType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        start: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        end: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        auxiliary: bool = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class CaselessSurfaceLoadResultantType:
    class Meta:
        name = "caseless_surface_load_resultant_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    load: list[LocationValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 3,
        },
    )
    resultant: list[ResultantType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 3,
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_type: ForceLoadType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    apply_on_ecc: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_dir: None | DirectionType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_sign: None | AutoForceSignType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_type: None | AutoForceTypeType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    assigned_structure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    load_projection: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CaselessSurfaceLoadType:
    class Meta:
        name = "caseless_surface_load_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    load: list[LocationValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_type: ForceLoadType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    apply_on_ecc: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_dir: None | DirectionType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_sign: None | AutoForceSignType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_type: None | AutoForceTypeType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    assigned_structure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    load_projection: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class CoverType:
    class Meta:
        name = "cover_type"

    load_bearing_direction: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    supporting_structures: None | CoverReferencelistType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class DiaphragmType:
    class Meta:
        name = "diaphragm_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="FS",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class ExtrudedFoundationType:
    class Meta:
        name = "extruded_foundation_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    cuboid_plinth: None | FoundationPlinthType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    thickness: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 10000.0,
        }
    )
    above: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class FootfallType:
    class Meta:
        name = "footfall_type"

    position: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    contour: None | ContourType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    region: None | RegionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    comment: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class InternalPanelType:
    class Meta:
        name = "internal_panel_type"

    region: None | RegionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    mesh_size: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e20,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class MovingLoadType:
    class Meta:
        name = "moving_load_type"

    division_points: None | PathDivisionNumberType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    division_distance: None | PathDivisionLengtType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    path_position: list[PointType3D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    local_y: list[PointType3D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    grid: None | MovingLoadGridType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    added_vehicle_position: list[PointType3D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    deleted_vehicle_position: list[PointType3D] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    vehicle_positions: None | MovingLoadType.VehiclePositions = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    vehicle: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    vehicle_shift_x: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        },
    )
    vehicle_shift_y: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -1000.0,
            "max_inclusive": 1000.0,
        },
    )
    return_value: bool = field(
        default=False,
        metadata={
            "name": "return",
            "type": "Attribute",
        },
    )
    lock_direction: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    cut_to_path: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class VehiclePositions:
        position: list[PointType3D] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
            },
        )


@dataclass(kw_only=True)
class PressureLoadType:
    class Meta:
        name = "pressure_load_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    load_type: ForceLoadType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    apply_on_ecc: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_dir: None | DirectionType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_sign: None | AutoForceSignType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    auto_force_type: None | AutoForceTypeType = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    assigned_structure: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    load_projection: bool = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    z0: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )
    q0: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )
    qh: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": -1e20,
            "max_inclusive": 1e20,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PunchingAreaType:
    class Meta:
        name = "punching_area_type"

    base_shell: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    connected_bar: list[GuidListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 2,
        },
    )
    local_pos: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    reference_points_offset: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    manual_design: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="PU",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    nodal_force_method: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    shell_internal_force_method: ShellForceType = field(
        default=ShellForceType.INTEGRATION,
        metadata={
            "type": "Attribute",
        },
    )
    distance_of_perimeter: float = field(
        default=1.5,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 3.0,
        },
    )
    perimeter_is_average: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PunchingAreaWallType:
    class Meta:
        name = "punching_area_wall_type"

    base_shell: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_pos: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    reference_points_offset: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    wall_base_ray: list[WbrType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    downward: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    manual_design: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="PU",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    shell_internal_force_method: ShellForceType = field(
        default=ShellForceType.INTEGRATION,
        metadata={
            "type": "Attribute",
        },
    )
    distance_of_perimeter: float = field(
        default=1.5,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 3.0,
        },
    )
    perimeter_length_limit: float = field(
        default=1000.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1.0,
            "max_inclusive": 1000.0,
        },
    )
    end_limit: float = field(
        default=1.5,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.5,
            "max_inclusive": 10.0,
        },
    )
    perimeter_is_average: bool = field(
        default=True,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PunchingReinforcementType:
    class Meta:
        name = "punching_reinforcement_type"

    base_shell: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    punching_area: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    bended_bar: None | PunchingReinforcementType.BendedBar = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    open_stirrups: None | PunchingReinforcementType.OpenStirrups = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    reinforcing_ring: None | PunchingReinforcementType.ReinforcingRing = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    stud_rails: None | PunchingReinforcementType.StudRails = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class BendedBar:
        local_center: PointType3D = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        wire: RfWireType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        tip_sections_length: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        middle_sections_length: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        height: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        angle: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
                "max_inclusive": 1.5707963267949,
            }
        )
        direction: DirectionType = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        c_v_auto_calculation: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
            },
        )
        c_v: float = field(
            default=0.0,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_inclusive": 10000.0,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class OpenStirrups:
        wire: RfWireType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        region: RegionType = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        width: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        length: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        height: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        distance_x: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        distance_y: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        c_v_auto_calculation: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
            },
        )
        c_v: float = field(
            default=0.0,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_inclusive": 10000.0,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class ReinforcingRing:
        auxiliary_reinforcement: PunchingReinforcementType.ReinforcingRing.AuxiliaryReinforcement = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        stirrups: PunchingReinforcementType.ReinforcingRing.Stirrups = field(
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "required": True,
            }
        )
        c_v_auto_calculation: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
            },
        )
        c_v: float = field(
            default=0.0,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_inclusive": 10000.0,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

        @dataclass(kw_only=True)
        class AuxiliaryReinforcement:
            wire: RfWireType = field(
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                    "required": True,
                }
            )
            inner_radius: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 0.0,
                }
            )
            overlap: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 0.0,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )

        @dataclass(kw_only=True)
        class Stirrups:
            wire: RfWireType = field(
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                    "required": True,
                }
            )
            width: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": 0.0,
                }
            )
            height: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": 0.0,
                }
            )
            max_distance: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": 0.0,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )

    @dataclass(kw_only=True)
    class StudRails:
        general_product: (
            None | PunchingReinforcementType.StudRails.GeneralProduct
        ) = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        peikko_psb_product: (
            None | PunchingReinforcementType.StudRails.PeikkoPsbProduct
        ) = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        pattern: StudrailPatterns = field(
            default=StudrailPatterns.SEMI_ORTHOGONAL,
            metadata={
                "type": "Attribute",
            },
        )
        auto_set_s0_s2: bool = field(
            default=False,
            metadata={
                "name": "auto_set_s0-s2",
                "type": "Attribute",
            },
        )
        s0: float = field(
            default=0.075,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.02,
                "max_inclusive": 10.0,
            },
        )
        s1: float = field(
            default=0.15,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.03,
                "max_inclusive": 10.0,
            },
        )
        s2: float = field(
            default=0.15,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.03,
                "max_inclusive": 10.0,
            },
        )
        rails_on_circle: int = field(
            default=12,
            metadata={
                "type": "Attribute",
                "min_inclusive": 4,
                "max_inclusive": 50,
            },
        )
        studs_on_rail: int = field(
            default=3,
            metadata={
                "type": "Attribute",
                "min_inclusive": 2,
                "max_inclusive": 50,
            },
        )
        height: None | float = field(
            default=None,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.01,
                "max_inclusive": 10.0,
            },
        )
        use_minimal_elements: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
            },
        )
        c_v_auto_calculation: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
            },
        )
        c_v: float = field(
            default=0.0,
            metadata={
                "type": "Attribute",
                "min_inclusive": 0.0,
                "max_inclusive": 10000.0,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

        @dataclass(kw_only=True)
        class GeneralProduct:
            wire: RfWireType = field(
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                    "required": True,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )

        @dataclass(kw_only=True)
        class PeikkoPsbProduct:
            psh: None | PshData = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "urn:strusoft",
                },
            )
            wire_diameter: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 0.001,
                    "max_inclusive": 0.1,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )


@dataclass(kw_only=True)
class RefplaneType:
    class Meta:
        name = "refplane_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="A",
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{1,256}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class RegionGroupType:
    class Meta:
        name = "region_group_type"

    region: list[RegionType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class RetainingWallType:
    class Meta:
        name = "retaining_wall_type"

    internal_entity: list[GuidListType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    slab_part: SlabPartType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SffoundationType:
    class Meta:
        name = "sffoundation_type"

    slab_part: SlabPartType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    referable_parts: None | SffoundationRefType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    insulation: None | FoundationInsulationType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="F",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    bedding_modulus: float = field(
        default=10000.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 100000000.0,
        },
    )
    analythical_system: SlabfoundationsystemsType = field(
        default=SlabfoundationsystemsType.SURFACE_SUPPORT_GROUP,
        metadata={
            "type": "Attribute",
        },
    )
    fillmode: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    fillcolor: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        },
    )
    bedding_modulus_x: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 100000000.0,
        },
    )
    bedding_modulus_y: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 100000000.0,
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SlabType1:
    class Meta:
        name = "slab_type"

    slab_part: list[SlabPartType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
        },
    )
    end: EmptyType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    type_value: Slabtype2 = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SurfaceConnectionType:
    class Meta:
        name = "surface_connection_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    rigidity: None | RigidityDataType1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    predefined_rigidity: None | ReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    ref: list[ReferenceType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    local_system: None | OptLocalsysType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="CS",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    distance: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": -10000.0,
            "max_inclusive": 10000.0,
        },
    )
    interface: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SurfaceRfType:
    class Meta:
        name = "surface_rf_type"

    base_shell: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    surface_reinforcement_parameters: GuidListType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    straight: None | SurfaceRfType.Straight = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    centric: None | SurfaceRfType.Centric = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    wire: RfWireType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    colour: str = field(
        default="0000a0",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    created_by: SrfTreatmentType = field(
        default=SrfTreatmentType.MANUAL,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Straight:
        direction: DirectionType = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
        space: float = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "min_exclusive": 0.0,
            }
        )
        face: None | SfRcFace = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        cover: float = field(
            default=0.02,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class Centric:
        radial: None | SurfaceRfType.Centric.Radial = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        tangential: None | SurfaceRfType.Centric.Tangential = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        face: None | SfRcFace = field(
            default=None,
            metadata={
                "type": "Attribute",
            },
        )
        cover: float = field(
            default=0.02,
            metadata={
                "type": "Attribute",
                "min_exclusive": 0.0,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

        @dataclass(kw_only=True)
        class Radial:
            angle: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_inclusive": 0.0,
                    "max_inclusive": 1.5707963267949,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )

        @dataclass(kw_only=True)
        class Tangential:
            space: float = field(
                metadata={
                    "type": "Attribute",
                    "required": True,
                    "min_exclusive": 0.0,
                }
            )
            any_attributes: dict[str, str] = field(
                default_factory=dict,
                metadata={
                    "type": "Attributes",
                    "namespace": "##any",
                },
            )


@dataclass(kw_only=True)
class SurfaceShearRfType:
    class Meta:
        name = "surface_shear_rf_type"

    wire: RfWireType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    base_shell: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    space_x: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 2.0,
        }
    )
    space_y: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.001,
            "max_inclusive": 2.0,
        }
    )
    colour: str = field(
        default="7b7bcc",
        metadata={
            "type": "Attribute",
            "pattern": r"[0-9A-Fa-f]{6}",
        },
    )
    created_by: SsrfTreatment = field(
        default=SsrfTreatment.MANUAL,
        metadata={
            "type": "Attribute",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SurfaceStressLoadType:
    class Meta:
        name = "surface_stress_load_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    stress: list[TopbottomValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SurfaceSupportLoadType:
    class Meta:
        name = "surface_support_load_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    displacement: list[LocationValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "min_occurs": 1,
            "max_occurs": 3,
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    load_type: MotionType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SurfaceSupportType:
    class Meta:
        name = "surface_support_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    mov_x: None | StiffBaseType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    mov_y: None | StiffBaseType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    mov_z: None | StiffBaseType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    plastic_limit_forces: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity: None | RigidityDataType1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    predefined_rigidity: None | ReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    rigidity_group: None | RigidityGroupType1 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    local_system: None | OptLocalsysType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="S",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    detach: str = field(
        default="",
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SurfaceTemperatureLoadType:
    class Meta:
        name = "surface_temperature_load_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    temperature: list[TopbottomValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 3,
        },
    )
    temperature_values: list[TopbottomValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "max_occurs": 3,
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    comment: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[ -#%'-;=?A-�]{0,1023}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class VirtualShellType:
    class Meta:
        name = "virtual_shell_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_pos: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_x: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_y: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    membrane_stiffness: StiffnessMatrix4Type = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    flexural_stiffness: StiffnessMatrix4Type = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    shear_stiffness: StiffnessMatrix2Type = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="FS",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    density: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    t1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    t2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    alfa_1: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    alfa_2: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 1e20,
        }
    )
    mesh_size: float = field(
        default=0.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1e20,
        },
    )
    ignore_in_st_imp_calculation: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class WlExternalWallType:
    class Meta:
        name = "wl_external_wall_type"

    at_0_degree: WlNtType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_90_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_180_degree: WlNtType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_270_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    base_shell: list[BsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    region: None | RegionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    direction_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    load_stripes: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 1,
            "max_inclusive": 1000,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class WlFlatRoofType:
    class Meta:
        name = "wl_flat_roof_type"

    at_0_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_90_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_180_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_270_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    base_shell: list[BsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    region: None | RegionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    angle: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 6.28318530717959,
        }
    )
    attic_walls_height: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_inclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class WlLeantoType:
    class Meta:
        name = "wl_leanto_type"

    at_0_degree: WlStType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_90_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_180_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_270_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    base_shell: list[BsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    region: None | RegionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    pressure_factor: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class WlRidgeRoofType:
    class Meta:
        name = "wl_ridge_roof_type"

    at_0_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_90_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_180_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    at_270_degree: WlTType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    base_shell: list[BsType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    region: None | RegionType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class PanelType1:
    class Meta:
        name = "panel_type"

    region: RegionType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    anchor_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    local_pos: None | PointType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    internal_panels: None | PanelType1.InternalPanels = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    timber_application_data: None | PanelType1.TimberApplicationData = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    camber_simulation: None | CamberType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    connections: None | PanelConnectionsType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    internal_plastic_limit_forces: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    internal_plastic_limit_moments: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    external_plastic_limit_forces: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    external_plastic_limit_moments: None | PlasticityType3D = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    internal_stiffness: None | StiffnessWithFriction = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    external_stiffness: None | StiffnessWithFriction = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    internal_rigidity: None | RigidityDataType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    internal_predefined_rigidity: None | ReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    internal_rigidity_group: None | RigidityGroupType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    external_rigidity: None | RigidityDataType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    external_predefined_rigidity: None | ReferenceType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    external_rigidity_group: None | RigidityGroupType3 = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    type_value: Paneltype2 = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    complex_material: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    complex_section: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    panelname: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    in_situ_fabricated: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    gap: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    orthotropy: float = field(
        default=1.0,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 1.0,
        },
    )
    thickness: float = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    alignment: VerAlign = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    align_offset: None | float = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ecc_calc: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    ecc_crack: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    internal_moving_local: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    external_moving_local: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    forced_plate: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    panel_width: float = field(
        default=1.5,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 100.0,
        },
    )
    panel_type: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    ignored_distance: float = field(
        default=0.02,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0.0,
            "max_inclusive": 10000.0,
        },
    )
    ignored_in_stability: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class InternalPanels:
        item: list[InternalPanelType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
                "min_occurs": 1,
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )

    @dataclass(kw_only=True)
    class TimberApplicationData:
        factors: None | TimberFactorsType = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "urn:strusoft",
            },
        )
        panel_type: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
                "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
            }
        )
        shear_coupling: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
            },
        )
        glued_narrow_sides: bool = field(
            default=True,
            metadata={
                "type": "Attribute",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )


@dataclass(kw_only=True)
class PtfoundationType:
    class Meta:
        name = "ptfoundation_type"

    connection_point: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    direction: PointType3D = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    polyhedron: None | PolyhedronType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    extruded_solid: None | ExtrudedFoundationType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    referable_parts: None | PtfoundationRefType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    insulation: None | FoundationInsulationType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    colouring: None | EntityColor = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        default="F",
        metadata={
            "type": "Attribute",
            "pattern": r"@{0,1}[ -#%'-;=?A-�]{0,50}(\.[0-9]{1,6}){0,2}",
        },
    )
    bedding_modulus: float = field(
        default=10000.0,
        metadata={
            "type": "Attribute",
            "min_exclusive": 0.0,
            "max_inclusive": 100000000.0,
        },
    )
    analythical_system: FoundationsystemsType = field(
        default=FoundationsystemsType.SIMPLE,
        metadata={
            "type": "Attribute",
        },
    )
    complex_material: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    fillmode: int = field(
        default=1,
        metadata={
            "type": "Attribute",
        },
    )
    fillcolor: int = field(
        default=0,
        metadata={
            "type": "Attribute",
        },
    )
    point_connections_stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    point_connections_end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    stage: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    end_stage: LastStageValue | int = field(
        default=LastStageValue.LAST_STAGE,
        metadata={
            "type": "Attribute",
            "min_inclusive": 1,
            "max_inclusive": 32767,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SectionType1:
    class Meta:
        name = "section_type"

    region_group: RegionGroupType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    end: EmptyType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    type_value: Sectiontype2 = field(
        metadata={
            "name": "type",
            "type": "Attribute",
            "required": True,
        }
    )
    fd_mat: FdMatType = field(
        default=FdMatType.VALUE_1_1,
        metadata={
            "name": "fd-mat",
            "type": "Attribute",
        },
    )
    fd_name_code: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fd_name_type: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fd_name_size: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    flags: int = field(
        default=1,
        metadata={
            "type": "Attribute",
            "min_inclusive": 0,
            "max_inclusive": 7,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SolidType:
    class Meta:
        name = "solid_type"

    facets: RegionGroupType = field(
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
            "required": True,
        }
    )
    style: None | StyleType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    guid: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class SurfaceLoadType(CaselessSurfaceLoadResultantType):
    class Meta:
        name = "surface_load_type"

    load_case: str | LcPtcType | LcPileType | LcFinalCs = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class VehicleLibType:
    class Meta:
        name = "vehicle_lib_type"

    point_load: list[CaselessPointLoadType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    line_load: list[CaselessLineLoadType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    surface_load: list[CaselessSurfaceLoadType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    name: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[ -#%'-;=?A-�]{1,255}",
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    last_change: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    action: ModificationType = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    hash_order_id: int = field(
        default=-1,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass(kw_only=True)
class FoundationType:
    class Meta:
        name = "foundation_type"

    isolated_foundation: list[PtfoundationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    wall_foundation: list[LnfoundationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )
    foundation_slab: list[SffoundationType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:strusoft",
        },
    )


@dataclass(kw_only=True)
class Database:
    class Meta:
        name = "database"
        namespace = "urn:strusoft"

    construction_stages: None | CsType = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    entities: None | Database.Entities = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    sections: None | Database.Sections = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    materials: None | Database.Materials = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reinforcing_materials: None | Database.ReinforcingMaterials = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    composites: None | Database.Composites = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    point_connection_types: None | Database.PointConnectionTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    point_support_group_types: None | Database.PointSupportGroupTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    line_connection_types: None | Database.LineConnectionTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    line_support_group_types: None | Database.LineSupportGroupTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    surface_connection_types: None | Database.SurfaceConnectionTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    surface_support_types: None | Database.SurfaceSupportTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    timber_panel_types: None | Database.TimberPanelTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    glc_panel_types: None | Database.GlcPanelTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    clt_panel_types: None | Database.CltPanelTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ptc_strand_types: None | Database.PtcStrandTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    vehicle_types: None | Database.VehicleTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bolt_types: None | Database.BoltTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    bar_end_releases_types: None | Database.BarEndReleasesTypes = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    geometry: None | Database.Geometry = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    user_defined_filter: list[UserfilterType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    user_defined_views: None | Database.UserDefinedViews = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    end: EmptyType = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
    struxml_version: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[0-9]{2}\.[0-9]{2}\.[0-9]{3}",
        }
    )
    source_software: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    start_time: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    end_time: XmlDateTime = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    guid: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        }
    )
    soil_as_solid: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
    hash: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{40}",
        },
    )
    convertid: str = field(
        default="00000000-0000-0000-0000-000000000000",
        metadata={
            "type": "Attribute",
            "pattern": r"[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}",
        },
    )
    standard: Standardtype = field(
        default=Standardtype.EC,
        metadata={
            "type": "Attribute",
        },
    )
    country: Eurocodetype = field(
        default=Eurocodetype.COMMON,
        metadata={
            "type": "Attribute",
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )

    @dataclass(kw_only=True)
    class Entities:
        foundations: list[FoundationType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        soil_elements: None | Database.Entities.SoilElements = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        retaining_wall: list[RetainingWallType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        bar: list[BarType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        column_corbel: list[ColumnCorbelType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        steel_bar_haunch: list[StbarHaunchType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        steel_bar_stiffener: list[StbarSiffenerType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        rc_beam_reduction_zone: list[BeamReductionZoneType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        hidden_bar: list[HiddenBarType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        bar_reinforcement: list[BarRfType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        slab: list[SlabType1] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        shell_buckling: list[ShellBucklingType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        wall_corbel: list[WallCorbelType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        surface_reinforcement_parameters: list[ShellRfParamsType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        surface_reinforcement: list[SurfaceRfType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        surface_reinforcement_single_by_line: list[SurfaceRfLineType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        surface_reinforcement_single_by_rectangle: list[SurfaceRfRectType] = (
            field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
        )
        punching_area: list[PunchingAreaType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        punching_area_wall: list[PunchingAreaWallType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        punching_reinforcement: list[PunchingReinforcementType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        no_shear_region: list[NoshearRegionType] = field(
            default_factory=list,
            metadata={
                "name": "no-shear_region",
                "type": "Element",
            },
        )
        shear_control_region: list[ShearControlRegionType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        surface_shear_reinforcement: list[SurfaceShearRfType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        panel: list[PanelType1] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        post_tensioned_cable: list[PtcType] = field(
            default_factory=list,
            metadata={
                "name": "post-tensioned_cable",
                "type": "Element",
            },
        )
        loads: None | Database.Entities.Loads = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        supports: None | Database.Entities.Supports = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        advanced_fem: None | Database.Entities.AdvancedFem = field(
            default=None,
            metadata={
                "name": "advanced-fem",
                "type": "Element",
            },
        )
        storeys: None | Database.Entities.Storeys = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        axes: None | Database.Entities.Axes = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        reference_planes: None | Database.Entities.ReferencePlanes = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        labelled_sections_geometry: (
            None | Database.Entities.LabelledSectionsGeometry
        ) = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        result_points: None | Database.Entities.ResultPoints = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        result_lines: None | Database.Entities.ResultLines = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        tsolids: None | Database.Entities.Tsolids = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )
        peak_smoothing_region: list[PsrType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        regions: None | Database.Entities.Regions = field(
            default=None,
            metadata={
                "type": "Element",
            },
        )

        @dataclass(kw_only=True)
        class SoilElements:
            strata: StrataType = field(
                metadata={
                    "type": "Element",
                    "required": True,
                }
            )
            borehole: list[BoreholeType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            filling: list[FillingType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            excavation: list[ExcavationType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            pile: list[PileType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class Loads:
            point_load: list[PointLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            line_load: list[LineLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            pressure_load: list[PressureLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            surface_load: list[SurfaceLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            line_temperature_variation_load: list[LineTemperatureLoadType] = (
                field(
                    default_factory=list,
                    metadata={
                        "type": "Element",
                    },
                )
            )
            surface_temperature_variation_load: list[
                SurfaceTemperatureLoadType
            ] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            line_stress_load: list[LineStressLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            surface_stress_load: list[SurfaceStressLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            point_support_motion_load: list[PointSupportLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            line_support_motion_load: list[LineSupportLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            surface_support_motion_load: list[SurfaceSupportLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            mass: list[MassPointType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            load_case_mass_conversion_table: None | MassConversionType = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            seismic_load: None | SeismicLoadType = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            ec_g2_seismic_load: None | EcG2SeismicLoadType = field(
                default=None,
                metadata={
                    "name": "EC_G2_seismic_load",
                    "type": "Element",
                },
            )
            footfall_analysis_data: list[FootfallType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            ground_acceleration: None | GroundAccelerationType = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            excitation_force: None | ExcitationForceType = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            periodic_excitation: None | PeriodicExcitationType = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            moving_load: list[MovingLoadType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            load_case: list[LoadCaseType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            load_combination: list[LoadCombinationType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            load_group_table: None | LoadGroupTable = field(
                default=None,
                metadata={
                    "type": "Element",
                },
            )
            wind_loads_external_wall: list[WlExternalWallType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            wind_loads_flat_roof: list[WlFlatRoofType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            wind_loads_lean_to: list[WlLeantoType] = field(
                default_factory=list,
                metadata={
                    "name": "wind_loads_lean-to",
                    "type": "Element",
                },
            )
            wind_loads_ridge_roof: list[WlRidgeRoofType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class Supports:
            point_support: list[PointSupportType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            line_support: list[LineSupportType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            surface_support: list[SurfaceSupportType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            stiffness_point: list[StiffnessPointType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class AdvancedFem:
            connected_points: list[ConnectedPointsType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            connected_lines: list[ConnectedLinesType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            surface_connection: list[SurfaceConnectionType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            virtual_bar: list[VirtualBarType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            virtual_shell: list[VirtualShellType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            diaphragm: list[DiaphragmType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            steel_joint: list[SteelJointType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            general_steel_joint: list[GenStjointType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            cover: list[CoverType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )
            building_cover: list[BuildingCoverType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                },
            )

        @dataclass(kw_only=True)
        class Storeys:
            storey: list[StoreyType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass(kw_only=True)
        class Axes:
            axis: list[AxisType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                    "max_occurs": 1024,
                },
            )

        @dataclass(kw_only=True)
        class ReferencePlanes:
            reference_plane: list[RefplaneType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass(kw_only=True)
        class LabelledSectionsGeometry:
            section_geometry: list[LabsecgeomType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass(kw_only=True)
        class ResultPoints:
            result_point: list[RespointType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass(kw_only=True)
        class ResultLines:
            result_line: list[ReslineType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass(kw_only=True)
        class Tsolids:
            polyhedron: list[PolyhedronType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

        @dataclass(kw_only=True)
        class Regions:
            region: list[DrawingRegionType] = field(
                default_factory=list,
                metadata={
                    "type": "Element",
                    "min_occurs": 1,
                },
            )

    @dataclass(kw_only=True)
    class Sections:
        section: list[SectionType1] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        complex_section: list[ComplexSectionType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class Materials:
        material: list[MaterialType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        complex_material: list[ComplexMaterialType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class ReinforcingMaterials:
        material: list[RfmaterialType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class Composites:
        composite_section: list[CompositeData] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        complex_composite: list[ComplexCompositeType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class PointConnectionTypes:
        predefined_type: list[RigidityDatalibType2] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class PointSupportGroupTypes:
        predefined_type: list[RigidityDatalibType2] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class LineConnectionTypes:
        predefined_type: list[RigidityDatalibType3] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class LineSupportGroupTypes:
        predefined_type: list[RigidityDatalibType2] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class SurfaceConnectionTypes:
        predefined_type: list[RigidityDatalibType1] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class SurfaceSupportTypes:
        predefined_type: list[RigidityDatalibType1] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class TimberPanelTypes:
        predefined_type: list[TimberpanelLibType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class GlcPanelTypes:
        predefined_type: list[GlcpanelLibType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class CltPanelTypes:
        predefined_type: list[CltpanelLibType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class PtcStrandTypes:
        predefined_type: list[PtcStrandLibType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class VehicleTypes:
        predefined_type: list[VehicleLibType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class BoltTypes:
        predefined_type: list[BoltLibType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class BarEndReleasesTypes:
        predefined_type: list[BarEndLibType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class Geometry:
        curve: list[CurveType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        point: list[PointType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        region: list[DrawingRegionType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        solid: list[SolidType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        text: list[TextType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        linear_dimension: list[DimlineType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        arc_dimension: list[DimarcType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        diameter_dimension: list[DimdiamType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        radius_dimension: list[DimradiusType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        angle_dimension: list[DimangleType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        level_dimension: list[DimfloorType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        line_type: list[LinetypeType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )
        layer: list[LayerType] = field(
            default_factory=list,
            metadata={
                "type": "Element",
            },
        )

    @dataclass(kw_only=True)
    class UserDefinedViews:
        view: list[ViewType1] = field(
            default_factory=list,
            metadata={
                "type": "Element",
                "min_occurs": 1,
                "max_occurs": 128,
            },
        )
        actual_view: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "pattern": r"[ -#%'-;=?A-�]{1,255}",
            },
        )
        physical_view: bool = field(
            default=False,
            metadata={
                "type": "Attribute",
            },
        )
        display_mode: Displaymodes = field(
            default=Displaymodes.WIREFRAME,
            metadata={
                "type": "Attribute",
            },
        )
        any_attributes: dict[str, str] = field(
            default_factory=dict,
            metadata={
                "type": "Attributes",
                "namespace": "##any",
            },
        )
