
# Single QUA script generated at 2025-07-16 14:20:12.150969
# QUA library version: 1.2.2

from qm import CompilerOptionArguments
from qm.qua import *

with program() as prog:
    v1 = declare(int, )
    v2 = declare(fixed, )
    v3 = declare(fixed, )
    with for_(v1,0,(v1<100),(v1+1)):
        r1 = declare_stream()
        save(v1, r1)
        reset_if_phase("q1.resonator")
        atr_r2 = declare_stream(adc_trace=True)
        measure("readout", "q1.resonator", dual_demod.full("iw1", "iw2", v2), dual_demod.full("iw3", "iw1", v3), adc_stream=atr_r2)
        wait(1000, "q1.resonator")
        align()
    with stream_processing():
        r1.save("n")
        atr_r2.input2().real().average().save("adcI1")
        atr_r2.input2().image().average().save("adcQ1")
        atr_r2.input2().real().save("adc_single_runI1")
        atr_r2.input2().image().save("adc_single_runQ1")


config = {
    "version": 1,
    "controllers": {
        "con1": {
            "fems": {
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "8": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "upconverter_frequency": 7050000000,
                        },
                        "2": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 5200000000.0,
                        },
                        "3": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 5200000000.0,
                        },
                        "4": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 5300000000.0,
                        },
                        "5": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 5000000000.0,
                        },
                        "6": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 5000000000.0,
                        },
                        "7": {
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "upconverter_frequency": 4700000000.0,
                        },
                    },
                    "analog_inputs": {
                        "2": {
                            "band": 2,
                            "downconverter_frequency": 7050000000,
                            "sampling_rate": 1000000000.0,
                            "shareable": False,
                        },
                    },
                },
            },
        },
    },
    "elements": {
        "q1.xy": {
            "operations": {
                "saturation": "q1.xy.saturation.pulse",
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "const": "q1.xy.const.pulse",
                "cr_square": "q1.xy.cr_square.pulse",
                "cr_flattop_0000": "q1.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q1.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q1.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q1.xy.cr_flattop_0060.pulse",
            },
            "intermediate_frequency": -92000000.0,
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
        },
        "q1.resonator": {
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "intermediate_frequency": 65700000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
        },
        "q2.xy": {
            "operations": {
                "saturation": "q2.xy.saturation.pulse",
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "const": "q2.xy.const.pulse",
                "cr_square": "q2.xy.cr_square.pulse",
                "cr_flattop_0000": "q2.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q2.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q2.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q2.xy.cr_flattop_0060.pulse",
            },
            "intermediate_frequency": -71700000.0,
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
        },
        "q2.resonator": {
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "intermediate_frequency": 115700000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
        },
        "q3.xy": {
            "operations": {
                "saturation": "q3.xy.saturation.pulse",
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "const": "q3.xy.const.pulse",
                "cr_square": "q3.xy.cr_square.pulse",
                "cr_flattop_0000": "q3.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q3.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q3.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q3.xy.cr_flattop_0060.pulse",
            },
            "intermediate_frequency": 123800000.0,
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
        },
        "q3.resonator": {
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "intermediate_frequency": 170800000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
        },
        "q4.xy": {
            "operations": {
                "saturation": "q4.xy.saturation.pulse",
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "const": "q4.xy.const.pulse",
                "cr_square": "q4.xy.cr_square.pulse",
                "cr_flattop_0000": "q4.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q4.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q4.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q4.xy.cr_flattop_0060.pulse",
            },
            "intermediate_frequency": 198500000.0,
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
        },
        "q4.resonator": {
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "intermediate_frequency": -193020000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
        },
        "q5.xy": {
            "operations": {
                "saturation": "q5.xy.saturation.pulse",
                "x180_DragCosine": "q5.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q5.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q5.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q5.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q5.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q5.xy.-y90_DragCosine.pulse",
                "x180": "q5.xy.x180_DragCosine.pulse",
                "x90": "q5.xy.x90_DragCosine.pulse",
                "-x90": "q5.xy.-x90_DragCosine.pulse",
                "y180": "q5.xy.y180_DragCosine.pulse",
                "y90": "q5.xy.y90_DragCosine.pulse",
                "-y90": "q5.xy.-y90_DragCosine.pulse",
                "const": "q5.xy.const.pulse",
                "cr_square": "q5.xy.cr_square.pulse",
                "cr_flattop_0000": "q5.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q5.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q5.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q5.xy.cr_flattop_0060.pulse",
            },
            "intermediate_frequency": -192270000.0,
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
        },
        "q5.resonator": {
            "operations": {
                "readout": "q5.resonator.readout.pulse",
                "const": "q5.resonator.const.pulse",
            },
            "intermediate_frequency": -143000000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
        },
        "q6.xy": {
            "operations": {
                "saturation": "q6.xy.saturation.pulse",
                "x180_DragCosine": "q6.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q6.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q6.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q6.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q6.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q6.xy.-y90_DragCosine.pulse",
                "x180": "q6.xy.x180_DragCosine.pulse",
                "x90": "q6.xy.x90_DragCosine.pulse",
                "-x90": "q6.xy.-x90_DragCosine.pulse",
                "y180": "q6.xy.y180_DragCosine.pulse",
                "y90": "q6.xy.y90_DragCosine.pulse",
                "-y90": "q6.xy.-y90_DragCosine.pulse",
                "const": "q6.xy.const.pulse",
                "cr_square": "q6.xy.cr_square.pulse",
                "cr_flattop_0000": "q6.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q6.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q6.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q6.xy.cr_flattop_0060.pulse",
            },
            "intermediate_frequency": -120937000.0,
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
        },
        "q6.resonator": {
            "operations": {
                "readout": "q6.resonator.readout.pulse",
                "const": "q6.resonator.const.pulse",
            },
            "intermediate_frequency": -94000000.0,
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
        },
        "cr_q1_q2": {
            "operations": {
                "square": "cr_q1_q2.square.pulse",
                "flattop_0000": "cr_q1_q2.flattop_0000.pulse",
                "flattop_0020": "cr_q1_q2.flattop_0020.pulse",
                "flattop_0040": "cr_q1_q2.flattop_0040.pulse",
                "flattop_0060": "cr_q1_q2.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
        },
        "cr_q4_q3": {
            "operations": {
                "square": "cr_q4_q3.square.pulse",
                "flattop_0000": "cr_q4_q3.flattop_0000.pulse",
                "flattop_0020": "cr_q4_q3.flattop_0020.pulse",
                "flattop_0040": "cr_q4_q3.flattop_0040.pulse",
                "flattop_0060": "cr_q4_q3.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
        },
        "zz_q4_q3": {
            "operations": {
                "square": "zz_q4_q3.square.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
        },
        "cr_q2_q1": {
            "operations": {
                "square": "cr_q2_q1.square.pulse",
                "flattop_0000": "cr_q2_q1.flattop_0000.pulse",
                "flattop_0020": "cr_q2_q1.flattop_0020.pulse",
                "flattop_0040": "cr_q2_q1.flattop_0040.pulse",
                "flattop_0060": "cr_q2_q1.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
        },
        "cr_q2_q3": {
            "operations": {
                "square": "cr_q2_q3.square.pulse",
                "flattop_0000": "cr_q2_q3.flattop_0000.pulse",
                "flattop_0020": "cr_q2_q3.flattop_0020.pulse",
                "flattop_0040": "cr_q2_q3.flattop_0040.pulse",
                "flattop_0060": "cr_q2_q3.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
        },
        "cr_q3_q2": {
            "operations": {
                "square": "cr_q3_q2.square.pulse",
                "flattop_0000": "cr_q3_q2.flattop_0000.pulse",
                "flattop_0020": "cr_q3_q2.flattop_0020.pulse",
                "flattop_0040": "cr_q3_q2.flattop_0040.pulse",
                "flattop_0060": "cr_q3_q2.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
        },
        "cr_q3_q4": {
            "operations": {
                "square": "cr_q3_q4.square.pulse",
                "flattop_0000": "cr_q3_q4.flattop_0000.pulse",
                "flattop_0020": "cr_q3_q4.flattop_0020.pulse",
                "flattop_0040": "cr_q3_q4.flattop_0040.pulse",
                "flattop_0060": "cr_q3_q4.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
        },
        "cr_q4_q5": {
            "operations": {
                "square": "cr_q4_q5.square.pulse",
                "flattop_0000": "cr_q4_q5.flattop_0000.pulse",
                "flattop_0020": "cr_q4_q5.flattop_0020.pulse",
                "flattop_0040": "cr_q4_q5.flattop_0040.pulse",
                "flattop_0060": "cr_q4_q5.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
        },
        "cr_q5_q4": {
            "operations": {
                "square": "cr_q5_q4.square.pulse",
                "flattop_0000": "cr_q5_q4.flattop_0000.pulse",
                "flattop_0020": "cr_q5_q4.flattop_0020.pulse",
                "flattop_0040": "cr_q5_q4.flattop_0040.pulse",
                "flattop_0060": "cr_q5_q4.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
        },
        "cr_q5_q6": {
            "operations": {
                "square": "cr_q5_q6.square.pulse",
                "flattop_0000": "cr_q5_q6.flattop_0000.pulse",
                "flattop_0020": "cr_q5_q6.flattop_0020.pulse",
                "flattop_0040": "cr_q5_q6.flattop_0040.pulse",
                "flattop_0060": "cr_q5_q6.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
        },
        "cr_q6_q5": {
            "operations": {
                "square": "cr_q6_q5.square.pulse",
                "flattop_0000": "cr_q6_q5.flattop_0000.pulse",
                "flattop_0020": "cr_q6_q5.flattop_0020.pulse",
                "flattop_0040": "cr_q6_q5.flattop_0040.pulse",
                "flattop_0060": "cr_q6_q5.flattop_0060.pulse",
            },
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
        },
        "q1.xy.saturation.pulse": {
            "operation": "control",
            "length": 30000,
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
        },
        "q1.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
        },
        "q1.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q1.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
        },
        "q1.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q1.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q1.xy.const.wf.I",
                "Q": "q1.xy.const.wf.Q",
            },
        },
        "q1.xy.cr_square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q1.xy.cr_square.wf.I",
                "Q": "q1.xy.cr_square.wf.Q",
            },
        },
        "q1.xy.cr_flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "q1.xy.cr_flattop_0000.wf.I",
                "Q": "q1.xy.cr_flattop_0000.wf.Q",
            },
        },
        "q1.xy.cr_flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "q1.xy.cr_flattop_0020.wf.I",
                "Q": "q1.xy.cr_flattop_0020.wf.Q",
            },
        },
        "q1.xy.cr_flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "q1.xy.cr_flattop_0040.wf.I",
                "Q": "q1.xy.cr_flattop_0040.wf.Q",
            },
        },
        "q1.xy.cr_flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "q1.xy.cr_flattop_0060.wf.I",
                "Q": "q1.xy.cr_flattop_0060.wf.Q",
            },
        },
        "q1.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
        },
        "q1.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
        },
        "q2.xy.saturation.pulse": {
            "operation": "control",
            "length": 30000,
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
        },
        "q2.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
        },
        "q2.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q2.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
        },
        "q2.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q2.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q2.xy.const.wf.I",
                "Q": "q2.xy.const.wf.Q",
            },
        },
        "q2.xy.cr_square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q2.xy.cr_square.wf.I",
                "Q": "q2.xy.cr_square.wf.Q",
            },
        },
        "q2.xy.cr_flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "q2.xy.cr_flattop_0000.wf.I",
                "Q": "q2.xy.cr_flattop_0000.wf.Q",
            },
        },
        "q2.xy.cr_flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "q2.xy.cr_flattop_0020.wf.I",
                "Q": "q2.xy.cr_flattop_0020.wf.Q",
            },
        },
        "q2.xy.cr_flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "q2.xy.cr_flattop_0040.wf.I",
                "Q": "q2.xy.cr_flattop_0040.wf.Q",
            },
        },
        "q2.xy.cr_flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "q2.xy.cr_flattop_0060.wf.I",
                "Q": "q2.xy.cr_flattop_0060.wf.Q",
            },
        },
        "q2.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
        },
        "q2.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
        },
        "q3.xy.saturation.pulse": {
            "operation": "control",
            "length": 30000,
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
        },
        "q3.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
        },
        "q3.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q3.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
        },
        "q3.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q3.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q3.xy.const.wf.I",
                "Q": "q3.xy.const.wf.Q",
            },
        },
        "q3.xy.cr_square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q3.xy.cr_square.wf.I",
                "Q": "q3.xy.cr_square.wf.Q",
            },
        },
        "q3.xy.cr_flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "q3.xy.cr_flattop_0000.wf.I",
                "Q": "q3.xy.cr_flattop_0000.wf.Q",
            },
        },
        "q3.xy.cr_flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "q3.xy.cr_flattop_0020.wf.I",
                "Q": "q3.xy.cr_flattop_0020.wf.Q",
            },
        },
        "q3.xy.cr_flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "q3.xy.cr_flattop_0040.wf.I",
                "Q": "q3.xy.cr_flattop_0040.wf.Q",
            },
        },
        "q3.xy.cr_flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "q3.xy.cr_flattop_0060.wf.I",
                "Q": "q3.xy.cr_flattop_0060.wf.Q",
            },
        },
        "q3.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q3.resonator.readout.wf.I",
                "Q": "q3.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q3.resonator.readout.iw1",
                "iw2": "q3.resonator.readout.iw2",
                "iw3": "q3.resonator.readout.iw3",
            },
        },
        "q3.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
            },
        },
        "q4.xy.saturation.pulse": {
            "operation": "control",
            "length": 30000,
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
        },
        "q4.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
        },
        "q4.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q4.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
        },
        "q4.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q4.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q4.xy.const.wf.I",
                "Q": "q4.xy.const.wf.Q",
            },
        },
        "q4.xy.cr_square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q4.xy.cr_square.wf.I",
                "Q": "q4.xy.cr_square.wf.Q",
            },
        },
        "q4.xy.cr_flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "q4.xy.cr_flattop_0000.wf.I",
                "Q": "q4.xy.cr_flattop_0000.wf.Q",
            },
        },
        "q4.xy.cr_flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "q4.xy.cr_flattop_0020.wf.I",
                "Q": "q4.xy.cr_flattop_0020.wf.Q",
            },
        },
        "q4.xy.cr_flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "q4.xy.cr_flattop_0040.wf.I",
                "Q": "q4.xy.cr_flattop_0040.wf.Q",
            },
        },
        "q4.xy.cr_flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "q4.xy.cr_flattop_0060.wf.I",
                "Q": "q4.xy.cr_flattop_0060.wf.Q",
            },
        },
        "q4.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q4.resonator.readout.wf.I",
                "Q": "q4.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q4.resonator.readout.iw1",
                "iw2": "q4.resonator.readout.iw2",
                "iw3": "q4.resonator.readout.iw3",
            },
        },
        "q4.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
            },
        },
        "q5.xy.saturation.pulse": {
            "operation": "control",
            "length": 30000,
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
        },
        "q5.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x180_DragCosine.wf.I",
                "Q": "q5.xy.x180_DragCosine.wf.Q",
            },
        },
        "q5.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q5.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
        },
        "q5.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-y90_DragCosine.wf.I",
                "Q": "q5.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q5.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q5.xy.const.wf.I",
                "Q": "q5.xy.const.wf.Q",
            },
        },
        "q5.xy.cr_square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q5.xy.cr_square.wf.I",
                "Q": "q5.xy.cr_square.wf.Q",
            },
        },
        "q5.xy.cr_flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "q5.xy.cr_flattop_0000.wf.I",
                "Q": "q5.xy.cr_flattop_0000.wf.Q",
            },
        },
        "q5.xy.cr_flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "q5.xy.cr_flattop_0020.wf.I",
                "Q": "q5.xy.cr_flattop_0020.wf.Q",
            },
        },
        "q5.xy.cr_flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "q5.xy.cr_flattop_0040.wf.I",
                "Q": "q5.xy.cr_flattop_0040.wf.Q",
            },
        },
        "q5.xy.cr_flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "q5.xy.cr_flattop_0060.wf.I",
                "Q": "q5.xy.cr_flattop_0060.wf.Q",
            },
        },
        "q5.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q5.resonator.readout.wf.I",
                "Q": "q5.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q5.resonator.readout.iw1",
                "iw2": "q5.resonator.readout.iw2",
                "iw3": "q5.resonator.readout.iw3",
            },
        },
        "q5.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q5.resonator.const.wf.I",
                "Q": "q5.resonator.const.wf.Q",
            },
        },
        "q6.xy.saturation.pulse": {
            "operation": "control",
            "length": 30000,
            "waveforms": {
                "I": "q6.xy.saturation.wf.I",
                "Q": "q6.xy.saturation.wf.Q",
            },
        },
        "q6.xy.x180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x180_DragCosine.wf.I",
                "Q": "q6.xy.x180_DragCosine.wf.Q",
            },
        },
        "q6.xy.x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x90_DragCosine.wf.I",
                "Q": "q6.xy.x90_DragCosine.wf.Q",
            },
        },
        "q6.xy.-x90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-x90_DragCosine.wf.I",
                "Q": "q6.xy.-x90_DragCosine.wf.Q",
            },
        },
        "q6.xy.y180_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y180_DragCosine.wf.I",
                "Q": "q6.xy.y180_DragCosine.wf.Q",
            },
        },
        "q6.xy.y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y90_DragCosine.wf.I",
                "Q": "q6.xy.y90_DragCosine.wf.Q",
            },
        },
        "q6.xy.-y90_DragCosine.pulse": {
            "operation": "control",
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-y90_DragCosine.wf.I",
                "Q": "q6.xy.-y90_DragCosine.wf.Q",
            },
        },
        "q6.xy.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q6.xy.const.wf.I",
                "Q": "q6.xy.const.wf.Q",
            },
        },
        "q6.xy.cr_square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "q6.xy.cr_square.wf.I",
                "Q": "q6.xy.cr_square.wf.Q",
            },
        },
        "q6.xy.cr_flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "q6.xy.cr_flattop_0000.wf.I",
                "Q": "q6.xy.cr_flattop_0000.wf.Q",
            },
        },
        "q6.xy.cr_flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "q6.xy.cr_flattop_0020.wf.I",
                "Q": "q6.xy.cr_flattop_0020.wf.Q",
            },
        },
        "q6.xy.cr_flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "q6.xy.cr_flattop_0040.wf.I",
                "Q": "q6.xy.cr_flattop_0040.wf.Q",
            },
        },
        "q6.xy.cr_flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "q6.xy.cr_flattop_0060.wf.I",
                "Q": "q6.xy.cr_flattop_0060.wf.Q",
            },
        },
        "q6.resonator.readout.pulse": {
            "operation": "measurement",
            "length": 1000,
            "digital_marker": "ON",
            "waveforms": {
                "I": "q6.resonator.readout.wf.I",
                "Q": "q6.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q6.resonator.readout.iw1",
                "iw2": "q6.resonator.readout.iw2",
                "iw3": "q6.resonator.readout.iw3",
            },
        },
        "q6.resonator.const.pulse": {
            "operation": "control",
            "length": 1000,
            "waveforms": {
                "I": "q6.resonator.const.wf.I",
                "Q": "q6.resonator.const.wf.Q",
            },
        },
        "cr_q1_q2.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q1_q2.square.wf.I",
                "Q": "cr_q1_q2.square.wf.Q",
            },
        },
        "cr_q1_q2.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q1_q2.flattop_0000.wf.I",
                "Q": "cr_q1_q2.flattop_0000.wf.Q",
            },
        },
        "cr_q1_q2.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q1_q2.flattop_0020.wf.I",
                "Q": "cr_q1_q2.flattop_0020.wf.Q",
            },
        },
        "cr_q1_q2.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q1_q2.flattop_0040.wf.I",
                "Q": "cr_q1_q2.flattop_0040.wf.Q",
            },
        },
        "cr_q1_q2.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q1_q2.flattop_0060.wf.I",
                "Q": "cr_q1_q2.flattop_0060.wf.Q",
            },
        },
        "cr_q4_q3.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q4_q3.square.wf.I",
                "Q": "cr_q4_q3.square.wf.Q",
            },
        },
        "cr_q4_q3.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q4_q3.flattop_0000.wf.I",
                "Q": "cr_q4_q3.flattop_0000.wf.Q",
            },
        },
        "cr_q4_q3.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q4_q3.flattop_0020.wf.I",
                "Q": "cr_q4_q3.flattop_0020.wf.Q",
            },
        },
        "cr_q4_q3.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q4_q3.flattop_0040.wf.I",
                "Q": "cr_q4_q3.flattop_0040.wf.Q",
            },
        },
        "cr_q4_q3.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q4_q3.flattop_0060.wf.I",
                "Q": "cr_q4_q3.flattop_0060.wf.Q",
            },
        },
        "zz_q4_q3.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "zz_q4_q3.square.wf.I",
                "Q": "zz_q4_q3.square.wf.Q",
            },
        },
        "cr_q2_q1.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q2_q1.square.wf.I",
                "Q": "cr_q2_q1.square.wf.Q",
            },
        },
        "cr_q2_q1.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q2_q1.flattop_0000.wf.I",
                "Q": "cr_q2_q1.flattop_0000.wf.Q",
            },
        },
        "cr_q2_q1.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q2_q1.flattop_0020.wf.I",
                "Q": "cr_q2_q1.flattop_0020.wf.Q",
            },
        },
        "cr_q2_q1.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q2_q1.flattop_0040.wf.I",
                "Q": "cr_q2_q1.flattop_0040.wf.Q",
            },
        },
        "cr_q2_q1.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q2_q1.flattop_0060.wf.I",
                "Q": "cr_q2_q1.flattop_0060.wf.Q",
            },
        },
        "cr_q2_q3.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q2_q3.square.wf.I",
                "Q": "cr_q2_q3.square.wf.Q",
            },
        },
        "cr_q2_q3.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q2_q3.flattop_0000.wf.I",
                "Q": "cr_q2_q3.flattop_0000.wf.Q",
            },
        },
        "cr_q2_q3.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q2_q3.flattop_0020.wf.I",
                "Q": "cr_q2_q3.flattop_0020.wf.Q",
            },
        },
        "cr_q2_q3.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q2_q3.flattop_0040.wf.I",
                "Q": "cr_q2_q3.flattop_0040.wf.Q",
            },
        },
        "cr_q2_q3.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q2_q3.flattop_0060.wf.I",
                "Q": "cr_q2_q3.flattop_0060.wf.Q",
            },
        },
        "cr_q3_q2.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q3_q2.square.wf.I",
                "Q": "cr_q3_q2.square.wf.Q",
            },
        },
        "cr_q3_q2.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q3_q2.flattop_0000.wf.I",
                "Q": "cr_q3_q2.flattop_0000.wf.Q",
            },
        },
        "cr_q3_q2.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q3_q2.flattop_0020.wf.I",
                "Q": "cr_q3_q2.flattop_0020.wf.Q",
            },
        },
        "cr_q3_q2.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q3_q2.flattop_0040.wf.I",
                "Q": "cr_q3_q2.flattop_0040.wf.Q",
            },
        },
        "cr_q3_q2.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q3_q2.flattop_0060.wf.I",
                "Q": "cr_q3_q2.flattop_0060.wf.Q",
            },
        },
        "cr_q3_q4.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q3_q4.square.wf.I",
                "Q": "cr_q3_q4.square.wf.Q",
            },
        },
        "cr_q3_q4.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q3_q4.flattop_0000.wf.I",
                "Q": "cr_q3_q4.flattop_0000.wf.Q",
            },
        },
        "cr_q3_q4.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q3_q4.flattop_0020.wf.I",
                "Q": "cr_q3_q4.flattop_0020.wf.Q",
            },
        },
        "cr_q3_q4.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q3_q4.flattop_0040.wf.I",
                "Q": "cr_q3_q4.flattop_0040.wf.Q",
            },
        },
        "cr_q3_q4.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q3_q4.flattop_0060.wf.I",
                "Q": "cr_q3_q4.flattop_0060.wf.Q",
            },
        },
        "cr_q4_q5.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q4_q5.square.wf.I",
                "Q": "cr_q4_q5.square.wf.Q",
            },
        },
        "cr_q4_q5.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q4_q5.flattop_0000.wf.I",
                "Q": "cr_q4_q5.flattop_0000.wf.Q",
            },
        },
        "cr_q4_q5.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q4_q5.flattop_0020.wf.I",
                "Q": "cr_q4_q5.flattop_0020.wf.Q",
            },
        },
        "cr_q4_q5.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q4_q5.flattop_0040.wf.I",
                "Q": "cr_q4_q5.flattop_0040.wf.Q",
            },
        },
        "cr_q4_q5.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q4_q5.flattop_0060.wf.I",
                "Q": "cr_q4_q5.flattop_0060.wf.Q",
            },
        },
        "cr_q5_q4.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q5_q4.square.wf.I",
                "Q": "cr_q5_q4.square.wf.Q",
            },
        },
        "cr_q5_q4.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q5_q4.flattop_0000.wf.I",
                "Q": "cr_q5_q4.flattop_0000.wf.Q",
            },
        },
        "cr_q5_q4.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q5_q4.flattop_0020.wf.I",
                "Q": "cr_q5_q4.flattop_0020.wf.Q",
            },
        },
        "cr_q5_q4.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q5_q4.flattop_0040.wf.I",
                "Q": "cr_q5_q4.flattop_0040.wf.Q",
            },
        },
        "cr_q5_q4.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q5_q4.flattop_0060.wf.I",
                "Q": "cr_q5_q4.flattop_0060.wf.Q",
            },
        },
        "cr_q5_q6.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q5_q6.square.wf.I",
                "Q": "cr_q5_q6.square.wf.Q",
            },
        },
        "cr_q5_q6.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q5_q6.flattop_0000.wf.I",
                "Q": "cr_q5_q6.flattop_0000.wf.Q",
            },
        },
        "cr_q5_q6.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q5_q6.flattop_0020.wf.I",
                "Q": "cr_q5_q6.flattop_0020.wf.Q",
            },
        },
        "cr_q5_q6.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q5_q6.flattop_0040.wf.I",
                "Q": "cr_q5_q6.flattop_0040.wf.Q",
            },
        },
        "cr_q5_q6.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q5_q6.flattop_0060.wf.I",
                "Q": "cr_q5_q6.flattop_0060.wf.Q",
            },
        },
        "cr_q6_q5.square.pulse": {
            "operation": "control",
            "length": 100,
            "waveforms": {
                "I": "cr_q6_q5.square.wf.I",
                "Q": "cr_q6_q5.square.wf.Q",
            },
        },
        "cr_q6_q5.flattop_0000.pulse": {
            "operation": "control",
            "length": 16,
            "waveforms": {
                "I": "cr_q6_q5.flattop_0000.wf.I",
                "Q": "cr_q6_q5.flattop_0000.wf.Q",
            },
        },
        "cr_q6_q5.flattop_0020.pulse": {
            "operation": "control",
            "length": 36,
            "waveforms": {
                "I": "cr_q6_q5.flattop_0020.wf.I",
                "Q": "cr_q6_q5.flattop_0020.wf.Q",
            },
        },
        "cr_q6_q5.flattop_0040.pulse": {
            "operation": "control",
            "length": 56,
            "waveforms": {
                "I": "cr_q6_q5.flattop_0040.wf.I",
                "Q": "cr_q6_q5.flattop_0040.wf.Q",
            },
        },
        "cr_q6_q5.flattop_0060.pulse": {
            "operation": "control",
            "length": 76,
            "waveforms": {
                "I": "cr_q6_q5.flattop_0060.wf.I",
                "Q": "cr_q6_q5.flattop_0060.wf.Q",
            },
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q1.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q1.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q1.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q1.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q1.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "q1.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q1.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "q1.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q1.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.039810717055349734,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q2.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q2.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q2.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q2.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "q2.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q2.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "q2.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q2.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q3.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q3.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q3.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q3.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "q3.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q3.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "q3.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q3.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q4.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q4.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q4.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q4.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "q4.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q4.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "q4.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q4.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q5.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q5.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q5.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q5.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "q5.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q5.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "q5.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q5.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q5.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q6.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
        },
        "q6.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q6.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q6.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "q6.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q6.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "q6.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q6.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "q6.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "q6.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "q6.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q6.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q6.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q1_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q1_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q1_q2.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q1_q2.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q1_q2.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q1_q2.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q1_q2.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q1_q2.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q1_q2.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q1_q2.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "cr_q4_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q4_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q4_q3.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q4_q3.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q4_q3.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q4_q3.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q4_q3.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q4_q3.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q4_q3.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q4_q3.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "zz_q4_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q4_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q1.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q2_q1.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q1.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q2_q1.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q2_q1.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q2_q1.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q2_q1.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q2_q1.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q2_q1.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q2_q1.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "cr_q2_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q2_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q3.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q2_q3.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q2_q3.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q2_q3.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q2_q3.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q2_q3.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q2_q3.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q2_q3.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "cr_q3_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q3_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q3_q2.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q3_q2.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q3_q2.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q3_q2.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q3_q2.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q3_q2.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q3_q2.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q3_q2.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "cr_q3_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q3_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q3_q4.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q3_q4.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q3_q4.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q3_q4.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q3_q4.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q3_q4.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q3_q4.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q3_q4.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "cr_q4_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q4_q5.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q4_q5.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q4_q5.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q4_q5.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q4_q5.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q4_q5.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q4_q5.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q4_q5.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q4_q5.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "cr_q5_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q5_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q5_q4.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q5_q4.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q5_q4.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q5_q4.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q5_q4.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q5_q4.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q5_q4.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q5_q4.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "cr_q5_q6.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q5_q6.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q5_q6.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q5_q6.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q5_q6.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q5_q6.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q5_q6.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q5_q6.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q5_q6.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q5_q6.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
        "cr_q6_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q6_q5.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q6_q5.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q6_q5.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
        },
        "cr_q6_q5.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q6_q5.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
        },
        "cr_q6_q5.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q6_q5.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
        },
        "cr_q6_q5.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
        },
        "cr_q6_q5.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [[1, 0]],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
    },
    "mixers": {},
    "oscillators": {},
}

loaded_config = {
    "version": 1,
    "controllers": {
        "con1": {
            "type": "opx1000",
            "fems": {
                "1": {
                    "type": "MW",
                    "analog_outputs": {
                        "8": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": 16,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 7050000000.0,
                                },
                            },
                        },
                        "2": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5200000000.0,
                                },
                            },
                        },
                        "3": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5200000000.0,
                                },
                            },
                        },
                        "4": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5300000000.0,
                                },
                            },
                        },
                        "5": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5000000000.0,
                                },
                            },
                        },
                        "6": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 5000000000.0,
                                },
                            },
                        },
                        "7": {
                            "sampling_rate": 1000000000.0,
                            "full_scale_power_dbm": -2,
                            "band": 2,
                            "delay": 0,
                            "shareable": False,
                            "upconverters": {
                                "1": {
                                    "frequency": 4700000000.0,
                                },
                            },
                        },
                    },
                    "analog_inputs": {
                        "2": {
                            "band": 2,
                            "shareable": False,
                            "gain_db": 0,
                            "sampling_rate": 1000000000.0,
                            "downconverter_frequency": 7050000000.0,
                        },
                    },
                },
            },
        },
    },
    "oscillators": {},
    "elements": {
        "q1.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q1.xy.saturation.pulse",
                "x180_DragCosine": "q1.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q1.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q1.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q1.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q1.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q1.xy.-y90_DragCosine.pulse",
                "x180": "q1.xy.x180_DragCosine.pulse",
                "x90": "q1.xy.x90_DragCosine.pulse",
                "-x90": "q1.xy.-x90_DragCosine.pulse",
                "y180": "q1.xy.y180_DragCosine.pulse",
                "y90": "q1.xy.y90_DragCosine.pulse",
                "-y90": "q1.xy.-y90_DragCosine.pulse",
                "const": "q1.xy.const.pulse",
                "cr_square": "q1.xy.cr_square.pulse",
                "cr_flattop_0000": "q1.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q1.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q1.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q1.xy.cr_flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
            "intermediate_frequency": -92000000.0,
        },
        "q1.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q1.resonator.readout.pulse",
                "const": "q1.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 28,
            "intermediate_frequency": 65700000.0,
        },
        "q2.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q2.xy.saturation.pulse",
                "x180_DragCosine": "q2.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q2.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q2.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q2.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q2.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q2.xy.-y90_DragCosine.pulse",
                "x180": "q2.xy.x180_DragCosine.pulse",
                "x90": "q2.xy.x90_DragCosine.pulse",
                "-x90": "q2.xy.-x90_DragCosine.pulse",
                "y180": "q2.xy.y180_DragCosine.pulse",
                "y90": "q2.xy.y90_DragCosine.pulse",
                "-y90": "q2.xy.-y90_DragCosine.pulse",
                "const": "q2.xy.const.pulse",
                "cr_square": "q2.xy.cr_square.pulse",
                "cr_flattop_0000": "q2.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q2.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q2.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q2.xy.cr_flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
            "intermediate_frequency": -71700000.0,
        },
        "q2.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q2.resonator.readout.pulse",
                "const": "q2.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "intermediate_frequency": 115700000.0,
        },
        "q3.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q3.xy.saturation.pulse",
                "x180_DragCosine": "q3.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q3.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q3.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q3.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q3.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q3.xy.-y90_DragCosine.pulse",
                "x180": "q3.xy.x180_DragCosine.pulse",
                "x90": "q3.xy.x90_DragCosine.pulse",
                "-x90": "q3.xy.-x90_DragCosine.pulse",
                "y180": "q3.xy.y180_DragCosine.pulse",
                "y90": "q3.xy.y90_DragCosine.pulse",
                "-y90": "q3.xy.-y90_DragCosine.pulse",
                "const": "q3.xy.const.pulse",
                "cr_square": "q3.xy.cr_square.pulse",
                "cr_flattop_0000": "q3.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q3.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q3.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q3.xy.cr_flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
            "intermediate_frequency": 123800000.0,
        },
        "q3.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q3.resonator.readout.pulse",
                "const": "q3.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "intermediate_frequency": 170800000.0,
        },
        "q4.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q4.xy.saturation.pulse",
                "x180_DragCosine": "q4.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q4.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q4.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q4.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q4.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q4.xy.-y90_DragCosine.pulse",
                "x180": "q4.xy.x180_DragCosine.pulse",
                "x90": "q4.xy.x90_DragCosine.pulse",
                "-x90": "q4.xy.-x90_DragCosine.pulse",
                "y180": "q4.xy.y180_DragCosine.pulse",
                "y90": "q4.xy.y90_DragCosine.pulse",
                "-y90": "q4.xy.-y90_DragCosine.pulse",
                "const": "q4.xy.const.pulse",
                "cr_square": "q4.xy.cr_square.pulse",
                "cr_flattop_0000": "q4.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q4.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q4.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q4.xy.cr_flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
            "intermediate_frequency": 198500000.0,
        },
        "q4.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q4.resonator.readout.pulse",
                "const": "q4.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "intermediate_frequency": -193020000.0,
        },
        "q5.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q5.xy.saturation.pulse",
                "x180_DragCosine": "q5.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q5.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q5.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q5.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q5.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q5.xy.-y90_DragCosine.pulse",
                "x180": "q5.xy.x180_DragCosine.pulse",
                "x90": "q5.xy.x90_DragCosine.pulse",
                "-x90": "q5.xy.-x90_DragCosine.pulse",
                "y180": "q5.xy.y180_DragCosine.pulse",
                "y90": "q5.xy.y90_DragCosine.pulse",
                "-y90": "q5.xy.-y90_DragCosine.pulse",
                "const": "q5.xy.const.pulse",
                "cr_square": "q5.xy.cr_square.pulse",
                "cr_flattop_0000": "q5.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q5.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q5.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q5.xy.cr_flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
            "intermediate_frequency": -192270000.0,
        },
        "q5.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q5.resonator.readout.pulse",
                "const": "q5.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "intermediate_frequency": -143000000.0,
        },
        "q6.xy": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "saturation": "q6.xy.saturation.pulse",
                "x180_DragCosine": "q6.xy.x180_DragCosine.pulse",
                "x90_DragCosine": "q6.xy.x90_DragCosine.pulse",
                "-x90_DragCosine": "q6.xy.-x90_DragCosine.pulse",
                "y180_DragCosine": "q6.xy.y180_DragCosine.pulse",
                "y90_DragCosine": "q6.xy.y90_DragCosine.pulse",
                "-y90_DragCosine": "q6.xy.-y90_DragCosine.pulse",
                "x180": "q6.xy.x180_DragCosine.pulse",
                "x90": "q6.xy.x90_DragCosine.pulse",
                "-x90": "q6.xy.-x90_DragCosine.pulse",
                "y180": "q6.xy.y180_DragCosine.pulse",
                "y90": "q6.xy.y90_DragCosine.pulse",
                "-y90": "q6.xy.-y90_DragCosine.pulse",
                "const": "q6.xy.const.pulse",
                "cr_square": "q6.xy.cr_square.pulse",
                "cr_flattop_0000": "q6.xy.cr_flattop_0000.pulse",
                "cr_flattop_0020": "q6.xy.cr_flattop_0020.pulse",
                "cr_flattop_0040": "q6.xy.cr_flattop_0040.pulse",
                "cr_flattop_0060": "q6.xy.cr_flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
            "intermediate_frequency": -120937000.0,
        },
        "q6.resonator": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "readout": "q6.resonator.readout.pulse",
                "const": "q6.resonator.const.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 8),
                "upconverter": 1,
            },
            "MWOutput": {
                "port": ('con1', 1, 2),
            },
            "smearing": 0,
            "time_of_flight": 32,
            "intermediate_frequency": -94000000.0,
        },
        "cr_q1_q2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q1_q2.square.pulse",
                "flattop_0000": "cr_q1_q2.flattop_0000.pulse",
                "flattop_0020": "cr_q1_q2.flattop_0020.pulse",
                "flattop_0040": "cr_q1_q2.flattop_0040.pulse",
                "flattop_0060": "cr_q1_q2.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 2),
                "upconverter": 1,
            },
        },
        "cr_q4_q3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q4_q3.square.pulse",
                "flattop_0000": "cr_q4_q3.flattop_0000.pulse",
                "flattop_0020": "cr_q4_q3.flattop_0020.pulse",
                "flattop_0040": "cr_q4_q3.flattop_0040.pulse",
                "flattop_0060": "cr_q4_q3.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
        },
        "zz_q4_q3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "zz_q4_q3.square.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
        },
        "cr_q2_q1": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q2_q1.square.pulse",
                "flattop_0000": "cr_q2_q1.flattop_0000.pulse",
                "flattop_0020": "cr_q2_q1.flattop_0020.pulse",
                "flattop_0040": "cr_q2_q1.flattop_0040.pulse",
                "flattop_0060": "cr_q2_q1.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
        },
        "cr_q2_q3": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q2_q3.square.pulse",
                "flattop_0000": "cr_q2_q3.flattop_0000.pulse",
                "flattop_0020": "cr_q2_q3.flattop_0020.pulse",
                "flattop_0040": "cr_q2_q3.flattop_0040.pulse",
                "flattop_0060": "cr_q2_q3.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 3),
                "upconverter": 1,
            },
        },
        "cr_q3_q2": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q3_q2.square.pulse",
                "flattop_0000": "cr_q3_q2.flattop_0000.pulse",
                "flattop_0020": "cr_q3_q2.flattop_0020.pulse",
                "flattop_0040": "cr_q3_q2.flattop_0040.pulse",
                "flattop_0060": "cr_q3_q2.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
        },
        "cr_q3_q4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q3_q4.square.pulse",
                "flattop_0000": "cr_q3_q4.flattop_0000.pulse",
                "flattop_0020": "cr_q3_q4.flattop_0020.pulse",
                "flattop_0040": "cr_q3_q4.flattop_0040.pulse",
                "flattop_0060": "cr_q3_q4.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 4),
                "upconverter": 1,
            },
        },
        "cr_q4_q5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q4_q5.square.pulse",
                "flattop_0000": "cr_q4_q5.flattop_0000.pulse",
                "flattop_0020": "cr_q4_q5.flattop_0020.pulse",
                "flattop_0040": "cr_q4_q5.flattop_0040.pulse",
                "flattop_0060": "cr_q4_q5.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 5),
                "upconverter": 1,
            },
        },
        "cr_q5_q4": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q5_q4.square.pulse",
                "flattop_0000": "cr_q5_q4.flattop_0000.pulse",
                "flattop_0020": "cr_q5_q4.flattop_0020.pulse",
                "flattop_0040": "cr_q5_q4.flattop_0040.pulse",
                "flattop_0060": "cr_q5_q4.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
        },
        "cr_q5_q6": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q5_q6.square.pulse",
                "flattop_0000": "cr_q5_q6.flattop_0000.pulse",
                "flattop_0020": "cr_q5_q6.flattop_0020.pulse",
                "flattop_0040": "cr_q5_q6.flattop_0040.pulse",
                "flattop_0060": "cr_q5_q6.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 6),
                "upconverter": 1,
            },
        },
        "cr_q6_q5": {
            "digitalInputs": {},
            "digitalOutputs": {},
            "outputs": {},
            "operations": {
                "square": "cr_q6_q5.square.pulse",
                "flattop_0000": "cr_q6_q5.flattop_0000.pulse",
                "flattop_0020": "cr_q6_q5.flattop_0020.pulse",
                "flattop_0040": "cr_q6_q5.flattop_0040.pulse",
                "flattop_0060": "cr_q6_q5.flattop_0060.pulse",
            },
            "hold_offset": {
                "duration": 0,
            },
            "sticky": {
                "analog": False,
                "digital": False,
                "duration": 4,
            },
            "MWInput": {
                "port": ('con1', 1, 7),
                "upconverter": 1,
            },
        },
    },
    "pulses": {
        "const_pulse": {
            "length": 1000,
            "waveforms": {
                "I": "const_wf",
                "Q": "zero_wf",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.saturation.pulse": {
            "length": 30000,
            "waveforms": {
                "I": "q1.xy.saturation.wf.I",
                "Q": "q1.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x180_DragCosine.wf.I",
                "Q": "q1.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.x90_DragCosine.wf.I",
                "Q": "q1.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-x90_DragCosine.wf.I",
                "Q": "q1.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y180_DragCosine.wf.I",
                "Q": "q1.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.y90_DragCosine.wf.I",
                "Q": "q1.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q1.xy.-y90_DragCosine.wf.I",
                "Q": "q1.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q1.xy.const.wf.I",
                "Q": "q1.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.cr_square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q1.xy.cr_square.wf.I",
                "Q": "q1.xy.cr_square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.cr_flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q1.xy.cr_flattop_0000.wf.I",
                "Q": "q1.xy.cr_flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.cr_flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "q1.xy.cr_flattop_0020.wf.I",
                "Q": "q1.xy.cr_flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.cr_flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "q1.xy.cr_flattop_0040.wf.I",
                "Q": "q1.xy.cr_flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.xy.cr_flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "q1.xy.cr_flattop_0060.wf.I",
                "Q": "q1.xy.cr_flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q1.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q1.resonator.readout.wf.I",
                "Q": "q1.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q1.resonator.readout.iw1",
                "iw2": "q1.resonator.readout.iw2",
                "iw3": "q1.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q1.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q1.resonator.const.wf.I",
                "Q": "q1.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.saturation.pulse": {
            "length": 30000,
            "waveforms": {
                "I": "q2.xy.saturation.wf.I",
                "Q": "q2.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x180_DragCosine.wf.I",
                "Q": "q2.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.x90_DragCosine.wf.I",
                "Q": "q2.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-x90_DragCosine.wf.I",
                "Q": "q2.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y180_DragCosine.wf.I",
                "Q": "q2.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.y90_DragCosine.wf.I",
                "Q": "q2.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q2.xy.-y90_DragCosine.wf.I",
                "Q": "q2.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q2.xy.const.wf.I",
                "Q": "q2.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.cr_square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q2.xy.cr_square.wf.I",
                "Q": "q2.xy.cr_square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.cr_flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q2.xy.cr_flattop_0000.wf.I",
                "Q": "q2.xy.cr_flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.cr_flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "q2.xy.cr_flattop_0020.wf.I",
                "Q": "q2.xy.cr_flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.cr_flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "q2.xy.cr_flattop_0040.wf.I",
                "Q": "q2.xy.cr_flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.xy.cr_flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "q2.xy.cr_flattop_0060.wf.I",
                "Q": "q2.xy.cr_flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q2.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q2.resonator.readout.wf.I",
                "Q": "q2.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q2.resonator.readout.iw1",
                "iw2": "q2.resonator.readout.iw2",
                "iw3": "q2.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q2.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q2.resonator.const.wf.I",
                "Q": "q2.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.saturation.pulse": {
            "length": 30000,
            "waveforms": {
                "I": "q3.xy.saturation.wf.I",
                "Q": "q3.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x180_DragCosine.wf.I",
                "Q": "q3.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.x90_DragCosine.wf.I",
                "Q": "q3.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-x90_DragCosine.wf.I",
                "Q": "q3.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y180_DragCosine.wf.I",
                "Q": "q3.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.y90_DragCosine.wf.I",
                "Q": "q3.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q3.xy.-y90_DragCosine.wf.I",
                "Q": "q3.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q3.xy.const.wf.I",
                "Q": "q3.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.cr_square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q3.xy.cr_square.wf.I",
                "Q": "q3.xy.cr_square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.cr_flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q3.xy.cr_flattop_0000.wf.I",
                "Q": "q3.xy.cr_flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.cr_flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "q3.xy.cr_flattop_0020.wf.I",
                "Q": "q3.xy.cr_flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.cr_flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "q3.xy.cr_flattop_0040.wf.I",
                "Q": "q3.xy.cr_flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.xy.cr_flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "q3.xy.cr_flattop_0060.wf.I",
                "Q": "q3.xy.cr_flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q3.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q3.resonator.readout.wf.I",
                "Q": "q3.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q3.resonator.readout.iw1",
                "iw2": "q3.resonator.readout.iw2",
                "iw3": "q3.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q3.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q3.resonator.const.wf.I",
                "Q": "q3.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.saturation.pulse": {
            "length": 30000,
            "waveforms": {
                "I": "q4.xy.saturation.wf.I",
                "Q": "q4.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x180_DragCosine.wf.I",
                "Q": "q4.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.x90_DragCosine.wf.I",
                "Q": "q4.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-x90_DragCosine.wf.I",
                "Q": "q4.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y180_DragCosine.wf.I",
                "Q": "q4.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.y90_DragCosine.wf.I",
                "Q": "q4.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q4.xy.-y90_DragCosine.wf.I",
                "Q": "q4.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q4.xy.const.wf.I",
                "Q": "q4.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.cr_square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q4.xy.cr_square.wf.I",
                "Q": "q4.xy.cr_square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.cr_flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q4.xy.cr_flattop_0000.wf.I",
                "Q": "q4.xy.cr_flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.cr_flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "q4.xy.cr_flattop_0020.wf.I",
                "Q": "q4.xy.cr_flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.cr_flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "q4.xy.cr_flattop_0040.wf.I",
                "Q": "q4.xy.cr_flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.xy.cr_flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "q4.xy.cr_flattop_0060.wf.I",
                "Q": "q4.xy.cr_flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q4.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q4.resonator.readout.wf.I",
                "Q": "q4.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q4.resonator.readout.iw1",
                "iw2": "q4.resonator.readout.iw2",
                "iw3": "q4.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q4.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q4.resonator.const.wf.I",
                "Q": "q4.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.saturation.pulse": {
            "length": 30000,
            "waveforms": {
                "I": "q5.xy.saturation.wf.I",
                "Q": "q5.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x180_DragCosine.wf.I",
                "Q": "q5.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.x90_DragCosine.wf.I",
                "Q": "q5.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-x90_DragCosine.wf.I",
                "Q": "q5.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y180_DragCosine.wf.I",
                "Q": "q5.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.y90_DragCosine.wf.I",
                "Q": "q5.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q5.xy.-y90_DragCosine.wf.I",
                "Q": "q5.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q5.xy.const.wf.I",
                "Q": "q5.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.cr_square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q5.xy.cr_square.wf.I",
                "Q": "q5.xy.cr_square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.cr_flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q5.xy.cr_flattop_0000.wf.I",
                "Q": "q5.xy.cr_flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.cr_flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "q5.xy.cr_flattop_0020.wf.I",
                "Q": "q5.xy.cr_flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.cr_flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "q5.xy.cr_flattop_0040.wf.I",
                "Q": "q5.xy.cr_flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.xy.cr_flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "q5.xy.cr_flattop_0060.wf.I",
                "Q": "q5.xy.cr_flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q5.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q5.resonator.readout.wf.I",
                "Q": "q5.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q5.resonator.readout.iw1",
                "iw2": "q5.resonator.readout.iw2",
                "iw3": "q5.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q5.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q5.resonator.const.wf.I",
                "Q": "q5.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.saturation.pulse": {
            "length": 30000,
            "waveforms": {
                "I": "q6.xy.saturation.wf.I",
                "Q": "q6.xy.saturation.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.x180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x180_DragCosine.wf.I",
                "Q": "q6.xy.x180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.x90_DragCosine.wf.I",
                "Q": "q6.xy.x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.-x90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-x90_DragCosine.wf.I",
                "Q": "q6.xy.-x90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.y180_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y180_DragCosine.wf.I",
                "Q": "q6.xy.y180_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.y90_DragCosine.wf.I",
                "Q": "q6.xy.y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.-y90_DragCosine.pulse": {
            "length": 40,
            "waveforms": {
                "I": "q6.xy.-y90_DragCosine.wf.I",
                "Q": "q6.xy.-y90_DragCosine.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q6.xy.const.wf.I",
                "Q": "q6.xy.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.cr_square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "q6.xy.cr_square.wf.I",
                "Q": "q6.xy.cr_square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.cr_flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "q6.xy.cr_flattop_0000.wf.I",
                "Q": "q6.xy.cr_flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.cr_flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "q6.xy.cr_flattop_0020.wf.I",
                "Q": "q6.xy.cr_flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.cr_flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "q6.xy.cr_flattop_0040.wf.I",
                "Q": "q6.xy.cr_flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.xy.cr_flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "q6.xy.cr_flattop_0060.wf.I",
                "Q": "q6.xy.cr_flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "q6.resonator.readout.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q6.resonator.readout.wf.I",
                "Q": "q6.resonator.readout.wf.Q",
            },
            "integration_weights": {
                "iw1": "q6.resonator.readout.iw1",
                "iw2": "q6.resonator.readout.iw2",
                "iw3": "q6.resonator.readout.iw3",
            },
            "operation": "measurement",
            "digital_marker": "ON",
        },
        "q6.resonator.const.pulse": {
            "length": 1000,
            "waveforms": {
                "I": "q6.resonator.const.wf.I",
                "Q": "q6.resonator.const.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q1_q2.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q1_q2.square.wf.I",
                "Q": "cr_q1_q2.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q1_q2.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q1_q2.flattop_0000.wf.I",
                "Q": "cr_q1_q2.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q1_q2.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q1_q2.flattop_0020.wf.I",
                "Q": "cr_q1_q2.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q1_q2.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q1_q2.flattop_0040.wf.I",
                "Q": "cr_q1_q2.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q1_q2.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q1_q2.flattop_0060.wf.I",
                "Q": "cr_q1_q2.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q3.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q4_q3.square.wf.I",
                "Q": "cr_q4_q3.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q3.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q4_q3.flattop_0000.wf.I",
                "Q": "cr_q4_q3.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q3.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q4_q3.flattop_0020.wf.I",
                "Q": "cr_q4_q3.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q3.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q4_q3.flattop_0040.wf.I",
                "Q": "cr_q4_q3.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q3.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q4_q3.flattop_0060.wf.I",
                "Q": "cr_q4_q3.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "zz_q4_q3.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "zz_q4_q3.square.wf.I",
                "Q": "zz_q4_q3.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q1.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q2_q1.square.wf.I",
                "Q": "cr_q2_q1.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q1.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q2_q1.flattop_0000.wf.I",
                "Q": "cr_q2_q1.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q1.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q2_q1.flattop_0020.wf.I",
                "Q": "cr_q2_q1.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q1.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q2_q1.flattop_0040.wf.I",
                "Q": "cr_q2_q1.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q1.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q2_q1.flattop_0060.wf.I",
                "Q": "cr_q2_q1.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q3.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q2_q3.square.wf.I",
                "Q": "cr_q2_q3.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q3.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q2_q3.flattop_0000.wf.I",
                "Q": "cr_q2_q3.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q3.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q2_q3.flattop_0020.wf.I",
                "Q": "cr_q2_q3.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q3.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q2_q3.flattop_0040.wf.I",
                "Q": "cr_q2_q3.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q2_q3.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q2_q3.flattop_0060.wf.I",
                "Q": "cr_q2_q3.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q2.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q3_q2.square.wf.I",
                "Q": "cr_q3_q2.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q2.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q3_q2.flattop_0000.wf.I",
                "Q": "cr_q3_q2.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q2.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q3_q2.flattop_0020.wf.I",
                "Q": "cr_q3_q2.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q2.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q3_q2.flattop_0040.wf.I",
                "Q": "cr_q3_q2.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q2.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q3_q2.flattop_0060.wf.I",
                "Q": "cr_q3_q2.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q4.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q3_q4.square.wf.I",
                "Q": "cr_q3_q4.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q4.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q3_q4.flattop_0000.wf.I",
                "Q": "cr_q3_q4.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q4.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q3_q4.flattop_0020.wf.I",
                "Q": "cr_q3_q4.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q4.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q3_q4.flattop_0040.wf.I",
                "Q": "cr_q3_q4.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q3_q4.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q3_q4.flattop_0060.wf.I",
                "Q": "cr_q3_q4.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q5.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q4_q5.square.wf.I",
                "Q": "cr_q4_q5.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q5.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q4_q5.flattop_0000.wf.I",
                "Q": "cr_q4_q5.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q5.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q4_q5.flattop_0020.wf.I",
                "Q": "cr_q4_q5.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q5.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q4_q5.flattop_0040.wf.I",
                "Q": "cr_q4_q5.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q4_q5.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q4_q5.flattop_0060.wf.I",
                "Q": "cr_q4_q5.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q4.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q5_q4.square.wf.I",
                "Q": "cr_q5_q4.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q4.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q5_q4.flattop_0000.wf.I",
                "Q": "cr_q5_q4.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q4.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q5_q4.flattop_0020.wf.I",
                "Q": "cr_q5_q4.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q4.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q5_q4.flattop_0040.wf.I",
                "Q": "cr_q5_q4.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q4.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q5_q4.flattop_0060.wf.I",
                "Q": "cr_q5_q4.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q6.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q5_q6.square.wf.I",
                "Q": "cr_q5_q6.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q6.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q5_q6.flattop_0000.wf.I",
                "Q": "cr_q5_q6.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q6.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q5_q6.flattop_0020.wf.I",
                "Q": "cr_q5_q6.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q6.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q5_q6.flattop_0040.wf.I",
                "Q": "cr_q5_q6.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q5_q6.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q5_q6.flattop_0060.wf.I",
                "Q": "cr_q5_q6.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q6_q5.square.pulse": {
            "length": 100,
            "waveforms": {
                "I": "cr_q6_q5.square.wf.I",
                "Q": "cr_q6_q5.square.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q6_q5.flattop_0000.pulse": {
            "length": 16,
            "waveforms": {
                "I": "cr_q6_q5.flattop_0000.wf.I",
                "Q": "cr_q6_q5.flattop_0000.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q6_q5.flattop_0020.pulse": {
            "length": 36,
            "waveforms": {
                "I": "cr_q6_q5.flattop_0020.wf.I",
                "Q": "cr_q6_q5.flattop_0020.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q6_q5.flattop_0040.pulse": {
            "length": 56,
            "waveforms": {
                "I": "cr_q6_q5.flattop_0040.wf.I",
                "Q": "cr_q6_q5.flattop_0040.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
        "cr_q6_q5.flattop_0060.pulse": {
            "length": 76,
            "waveforms": {
                "I": "cr_q6_q5.flattop_0060.wf.I",
                "Q": "cr_q6_q5.flattop_0060.wf.Q",
            },
            "integration_weights": {},
            "operation": "control",
        },
    },
    "waveforms": {
        "zero_wf": {
            "type": "constant",
            "sample": 0.0,
        },
        "const_wf": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q1.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q1.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q1.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q1.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.039810717055349734,
        },
        "q1.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q1.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q1.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q2.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q2.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q2.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q2.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q2.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q2.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q3.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q3.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q3.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q3.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q3.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q3.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q4.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q4.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q4.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q4.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q4.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q4.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q5.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q5.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q5.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q5.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q5.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q5.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.saturation.wf.I": {
            "type": "constant",
            "sample": 0.17740669461678774,
        },
        "q6.xy.saturation.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.x180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 40,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-x90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 1.406733470668225e-19, 5.590500224705675e-19, 1.2442942900814307e-18, 2.1786586833105406e-18, 3.337943655172292e-18, 4.692124333839833e-18, 6.2061281510540535e-18, 7.840743203218705e-18, 9.553633819106502e-18, 1.1300437031505974e-17, 1.3035911554769475e-17, 1.4715109510347304e-17, 1.6294540553232083e-17, 1.773329824905003e-17, 1.8994119529224112e-17, 2.0044349784876754e-17, 2.0856788604047122e-17, 2.1410394248073164e-17, 2.169082862157027e-17, 2.1690828621570273e-17, 2.1410394248073164e-17, 2.0856788604047122e-17, 2.0044349784876763e-17, 1.8994119529224118e-17, 1.773329824905003e-17, 1.6294540553232074e-17, 1.471510951034731e-17, 1.303591155476948e-17, 1.1300437031505974e-17, 9.55363381910651e-18, 7.840743203218713e-18, 6.206128151054058e-18, 4.6921243338398365e-18, 3.337943655172293e-18, 2.1786586833105406e-18, 1.2442942900814297e-18, 5.590500224705664e-19, 1.406733470668225e-19, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y180_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.002297370101563402, 0.009129979727376088, 0.020320867877134156, 0.03558019642606191, 0.05451275678009853, 0.07662820557089069, 0.10135376429146757, 0.12804905395870445, 0.15602268059261026, 0.18455014195723662, 0.2128925917880255, 0.24031597552196335, 0.2661100419251816, 0.2896067382268364, 0.3101975123349615, 0.3273490740159924, 0.34061720683169106, 0.3496582731115602, 0.35423811398800487, 0.3542381139880049, 0.3496582731115602, 0.34061720683169106, 0.3273490740159925, 0.3101975123349616, 0.2896067382268364, 0.2661100419251815, 0.24031597552196343, 0.21289259178802555, 0.18455014195723662, 0.1560226805926104, 0.12804905395870456, 0.10135376429146765, 0.07662820557089074, 0.054512756780098544, 0.03558019642606191, 0.02032086787713414, 0.009129979727376069, 0.002297370101563402, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, 0.001148685050781701, 0.004564989863688044, 0.010160433938567078, 0.017790098213030955, 0.027256378390049265, 0.03831410278544534, 0.050676882145733786, 0.06402452697935222, 0.07801134029630513, 0.09227507097861831, 0.10644629589401275, 0.12015798776098167, 0.1330550209625908, 0.1448033691134182, 0.15509875616748076, 0.1636745370079962, 0.17030860341584553, 0.1748291365557801, 0.17711905699400243, 0.17711905699400246, 0.1748291365557801, 0.17030860341584553, 0.16367453700799625, 0.1550987561674808, 0.1448033691134182, 0.13305502096259075, 0.12015798776098172, 0.10644629589401278, 0.09227507097861831, 0.0780113402963052, 0.06402452697935228, 0.05067688214573383, 0.03831410278544537, 0.027256378390049272, 0.017790098213030955, 0.01016043393856707, 0.0045649898636880345, 0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.I": {
            "type": "arbitrary",
            "samples": [0.0, 7.033667353341125e-20, 2.7952501123528376e-19, 6.221471450407153e-19, 1.0893293416552703e-18, 1.668971827586146e-18, 2.3460621669199163e-18, 3.1030640755270267e-18, 3.9203716016093525e-18, 4.776816909553251e-18, 5.650218515752987e-18, 6.517955777384738e-18, 7.357554755173652e-18, 8.147270276616041e-18, 8.866649124525015e-18, 9.497059764612056e-18, 1.0022174892438377e-17, 1.0428394302023561e-17, 1.0705197124036582e-17, 1.0845414310785135e-17, 1.0845414310785137e-17, 1.0705197124036582e-17, 1.0428394302023561e-17, 1.0022174892438381e-17, 9.497059764612059e-18, 8.866649124525015e-18, 8.147270276616037e-18, 7.357554755173655e-18, 6.51795577738474e-18, 5.650218515752987e-18, 4.776816909553255e-18, 3.9203716016093564e-18, 3.103064075527029e-18, 2.3460621669199183e-18, 1.6689718275861464e-18, 1.0893293416552703e-18, 6.221471450407149e-19, 2.795250112352832e-19, 7.033667353341125e-20, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.-y90_DragCosine.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0, -0.001148685050781701, -0.004564989863688044, -0.010160433938567078, -0.017790098213030955, -0.027256378390049265, -0.03831410278544534, -0.050676882145733786, -0.06402452697935222, -0.07801134029630513, -0.09227507097861831, -0.10644629589401275, -0.12015798776098167, -0.1330550209625908, -0.1448033691134182, -0.15509875616748076, -0.1636745370079962, -0.17030860341584553, -0.1748291365557801, -0.17711905699400243, -0.17711905699400246, -0.1748291365557801, -0.17030860341584553, -0.16367453700799625, -0.1550987561674808, -0.1448033691134182, -0.13305502096259075, -0.12015798776098172, -0.10644629589401278, -0.09227507097861831, -0.0780113402963052, -0.06402452697935228, -0.05067688214573383, -0.03831410278544537, -0.027256378390049272, -0.017790098213030955, -0.01016043393856707, -0.0045649898636880345, -0.001148685050781701, 0.0],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q6.xy.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.cr_square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "q6.xy.cr_square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.xy.cr_flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.cr_flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.cr_flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.cr_flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.cr_flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.cr_flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.cr_flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.xy.cr_flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "q6.resonator.readout.wf.I": {
            "type": "constant",
            "sample": 0.0446683592150963,
        },
        "q6.resonator.readout.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "q6.resonator.const.wf.I": {
            "type": "constant",
            "sample": 0.5,
        },
        "q6.resonator.const.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q1_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q1_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q1_q2.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q1_q2.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q1_q2.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q1_q2.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q1_q2.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q1_q2.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q1_q2.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q1_q2.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q4_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q4_q3.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q3.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q3.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q3.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q3.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q3.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q3.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q3.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "zz_q4_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "zz_q4_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q1.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q2_q1.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q1.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q1.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q1.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q1.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q1.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q1.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q1.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q1.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q3.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q2_q3.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q2_q3.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q3.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q3.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q3.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q3.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q3.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q3.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q2_q3.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q2.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q3_q2.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q3_q2.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q2.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q2.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q2.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q2.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q2.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q2.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q2.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q3_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q3_q4.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q4.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q4.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q4.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q4.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q4.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q4.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q3_q4.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q4_q5.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q4_q5.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q5.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q5.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q5.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q5.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q5.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q5.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q4_q5.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q4.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q5_q4.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q5_q4.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q4.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q4.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q4.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q4.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q4.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q4.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q4.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q6.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q5_q6.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q5_q6.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q6.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q6.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q6.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q6.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q6.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q6.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q5_q6.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q6_q5.square.wf.I": {
            "type": "constant",
            "sample": 0.1,
        },
        "cr_q6_q5.square.wf.Q": {
            "type": "constant",
            "sample": 0.0,
        },
        "cr_q6_q5.flattop_0000.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955] + [0.09523447998951765] * 2 + [0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q6_q5.flattop_0000.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 16,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q6_q5.flattop_0020.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 20 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q6_q5.flattop_0020.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 36,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q6_q5.flattop_0040.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 40 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q6_q5.flattop_0040.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 56,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q6_q5.flattop_0060.wf.I": {
            "type": "arbitrary",
            "samples": [1.6931612436130023e-06, 2.607487846688273e-05, 0.0002717064729323586, 0.0019157171837129155, 0.009139375535604729, 0.02950226561744429, 0.06443887248251955, 0.09523447998951765] + [0.1] * 60 + [0.09523447998951765, 0.06443887248251955, 0.02950226561744429, 0.009139375535604729, 0.0019157171837129155, 0.0002717064729323586, 2.607487846688273e-05, 1.6931612436130023e-06],
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
        "cr_q6_q5.flattop_0060.wf.Q": {
            "type": "arbitrary",
            "samples": [0.0] * 76,
            "is_overridable": False,
            "max_allowed_error": 0.0001,
        },
    },
    "digital_waveforms": {
        "ON": {
            "samples": [(1, 0)],
        },
    },
    "integration_weights": {
        "q1.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q1.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q1.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q2.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q2.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q2.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q3.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q3.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q3.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q4.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q4.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q4.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q5.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q5.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q5.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
        "q6.resonator.readout.iw1": {
            "cosine": [(1.0, 1000)],
            "sine": [(-0.0, 1000)],
        },
        "q6.resonator.readout.iw2": {
            "cosine": [(0.0, 1000)],
            "sine": [(1.0, 1000)],
        },
        "q6.resonator.readout.iw3": {
            "cosine": [(-0.0, 1000)],
            "sine": [(-1.0, 1000)],
        },
    },
    "mixers": {},
}


