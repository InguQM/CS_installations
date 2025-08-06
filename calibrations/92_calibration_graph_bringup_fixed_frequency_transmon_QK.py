# %%
from typing import List
from qualibrate.orchestration.basic_orchestrator import BasicOrchestrator
from qualibrate.parameters import GraphParameters
from qualibrate.qualibration_graph import QualibrationGraph
from qualibrate.qualibration_library import QualibrationLibrary

library = QualibrationLibrary.get_active_library()


class Parameters(GraphParameters):
    qubits: List[str] =  ["q1","q2","q7","q8","q9","q10","q11","q12","q16","q17","q18","q19","q20","q21","q24","q25","q26"]

g = QualibrationGraph(
    name="FixedFrequencyTransmon_BringUp_QK",
    parameters=Parameters(),
    nodes={
        "resonator_spectroscopy": library.nodes["02a_resonator_spectroscopy"].copy(
            name="resonator_spectroscopy",    
            num_shots = 100,
            frequency_span_in_mhz = 10,
            frequency_step_in_mhz = 0.05,
            multiplexed =True,
        ),
            # "resonator_spectroscopy_vs_power": library.nodes["02b_resonator_spectroscopy_vs_power"].copy(name="resonator_spectroscopy_vs_power"),
        "qubit_spectroscopy": library.nodes["03a_qubit_spectroscopy"].copy(
            name="qubit_spectroscopy",
            num_shots = 100,
            frequency_span_in_mhz = 6,
            frequency_step_in_mhz = 0.05,
            operation = "saturation",
            operation_amplitude_factor = 0.01,
            operation_len_in_ns = None,
            target_peak_width = 2e5,
            update_pulses_amplitude = False,
            multiplexed =True,
        ),
        # "rabi_chevron": library.nodes["04a_rabi_chevron"].copy(name="rabi_chevron"),
        # "power_rabi": 
        #     library.nodes["04b_power_rabi"].copy(name="power_rabi",
        #     num_shots = 40,
        #     operation = "x180",
        #     min_amp_factor = 0.8,
        #     max_amp_factor = 1.2,
        #     amp_factor_step = 0.02,
        #     max_number_pulses_per_sweep = 1,
        #     update_x90 = True,
        #     ),
        # "readout_power_optimization": library.nodes["08b_readout_power_optimization"].copy(
        #     name="readout_power_optimization",
        #     num_shots = 2000,
        #     start_amp = 0.5,
        #     end_amp = 1.99,
        #     num_amps = 10,
        #     outliers_threshold = 0.98,
        #     plot_raw = False,
        #     multiplexed =True,
        # ),
        # "readout_frequency_optimization": library.nodes["08a_readout_frequency_optimization"].copy(
        #     name="readout_frequency_optimization",
        #     num_shots = 100,
        #     frequency_span_in_mhz = 10,
        #     frequency_step_in_mhz = 0.1,
        #     multiplexed =True,
        # ),
        "IQ_blobs": library.nodes["07_iq_blobs"].copy(name="IQ_blobs",    
            num_shots = 200,
            operation= "readout",
            multiplexed =True),
        # "power_rabi_error_amplification_x180": library.nodes["04b_power_rabi"].copy(
        #     name="power_rabi_error_amplification_x180",
        #     max_number_pulses_per_sweep=50,
        #     min_amp_factor=0.8,
        #     max_amp_factor=1.2,
        #     amp_factor_step=0.02,
        #     use_state_discrimination=True,
        # ),
        # "power_rabi_error_amplification_x90": library.nodes["04b_power_rabi"].copy(
        #     name="power_rabi_error_amplification_x90",
        #     max_number_pulses_per_sweep=50,
        #     min_amp_factor=0.8,
        #     max_amp_factor=1.2,
        #     amp_factor_step=0.02,
        #     operation="x90",
        #     update_x90=False,
        #     use_state_discrimination=True,
        # ),
        "T1": library.nodes["05_T1"].copy(name="T1", 
            use_state_discrimination=True,    
            num_shots = 100,
            min_wait_time_in_ns = 24),
        # "ramsey": library.nodes["06a_ramsey"].copy(name="ramsey", use_state_discrimination=True,
        #     num_shots = 100,
        #     frequency_detuning_in_mhz = 1.0,
        #     min_wait_time_in_ns = 16,
        #     max_wait_time_in_ns = 50000,
        #     wait_time_num_points = 500,
        #     log_or_linear_sweep = "linear"
        #     ),
        "T2echo": library.nodes["06b_echo"].copy(name="T2echo", use_state_discrimination=True,
            num_shots = 100,
            log_or_linear_sweep = "log"),
        # "DRAG_calibration": library.nodes["10b_drag_calibration_180_minus_180"].copy(
        #     name="DRAG_calibration", use_state_discrimination=True,
        #     num_shots = 10,
        #     operation = "x180",
        #     min_amp_factor = -1,
        #     max_amp_factor = 2.0,
        #     amp_factor_step = 0.02,
        #     max_number_pulses_per_sweep = 40,
        #     alpha_setpoint= None,
        #     multiplexed =True,
        # ),
        "Randomized_benchmarking": library.nodes["11a_single_qubit_randomized_benchmarking"].copy(
            name="Randomized_benchmarking",  
            use_state_discrimination = True,
            use_strict_timing = False,
            num_random_sequences = 64,
            num_shots = 20,
            max_circuit_depth = 1600,
            delta_clifford = 40,
            seed = None,
            multiplexed =True,
        ),
    },
    connectivity=[
        ("resonator_spectroscopy", "qubit_spectroscopy"),
        ("qubit_spectroscopy", "T1"),

        ("T1", "IQ_blobs"),
        # ("qubit_spectroscopy", "IQ_blobs"),
        ("IQ_blobs", "T2echo"),
        
        ("T2echo", "Randomized_benchmarking")
    ],
    orchestrator=BasicOrchestrator(skip_failed=False),
)

g.run()

# %%