# Python 3.13 Compatible
print("\n\033[32mInitializing ControlAltAI Nodes\033[0m")  # Fixed green reset

try:
    from .megapixel_calculator_node import MegapixelCalculatorNode
    from .flux_sampler_node import FluxSampler
    from .flux_union_controlnet_node import FluxUnionControlNetApply
    from .boolean_basic_node import BooleanBasic
    from .boolean_reverse_node import BooleanReverse
    from .get_image_size_ratio_node import GetImageSizeRatio
    from .noise_plus_blend_node import NoisePlusBlend
    from .integer_settings_node import IntegerSettings
    from .integer_settings_advanced_node import IntegerSettingsAdvanced
    from .choose_upscale_model_node import ChooseUpscaleModel
    from .region_mask_generator_node import RegionMaskGenerator
    from .region_mask_validator_node import RegionMaskValidator
    from .region_mask_processor_node import RegionMaskProcessor
    from .region_mask_conditioning_node import RegionMaskConditioning
    from .flux_attention_control_node import FluxAttentionControl
    from .region_overlay_visualizer_node import RegionOverlayVisualizer
    from .flux_attention_cleanup_node import FluxAttentionCleanup
    from .hidream_resolution_node import HiDreamResolutionNode
    from .perturbation_texture_node import PerturbationTexture
    from .text_bridge_node import TextBridge
    from .two_way_switch_node import TwoWaySwitch
    from .three_way_switch_node import ThreeWaySwitch
except ImportError:
    # Fallback to absolute imports for Python 3.13 compatibility
    from megapixel_calculator_node import MegapixelCalculatorNode
    from flux_sampler_node import FluxSampler
    from flux_union_controlnet_node import FluxUnionControlNetApply
    from boolean_basic_node import BooleanBasic
    from boolean_reverse_node import BooleanReverse
    from get_image_size_ratio_node import GetImageSizeRatio
    from noise_plus_blend_node import NoisePlusBlend
    from integer_settings_node import IntegerSettings
    from integer_settings_advanced_node import IntegerSettingsAdvanced
    from choose_upscale_model_node import ChooseUpscaleModel
    from region_mask_generator_node import RegionMaskGenerator
    from region_mask_validator_node import RegionMaskValidator
    from region_mask_processor_node import RegionMaskProcessor
    from region_mask_conditioning_node import RegionMaskConditioning
    from flux_attention_control_node import FluxAttentionControl
    from region_overlay_visualizer_node import RegionOverlayVisualizer
    from flux_attention_cleanup_node import FluxAttentionCleanup
    from hidream_resolution_node import HiDreamResolutionNode
    from perturbation_texture_node import PerturbationTexture
    from text_bridge_node import TextBridge
    from two_way_switch_node import TwoWaySwitch
    from three_way_switch_node import ThreeWaySwitch

NODE_CLASS_MAPPINGS = {
    "MegapixelCalculatorNode": MegapixelCalculatorNode,
    "FluxSampler": FluxSampler,
    "FluxUnionControlNetApply": FluxUnionControlNetApply,
    "BooleanBasic": BooleanBasic,
    "BooleanReverse": BooleanReverse,
    "GetImageSizeRatio": GetImageSizeRatio,
    "NoisePlusBlend": NoisePlusBlend,
    "IntegerSettings": IntegerSettings,
    "IntegerSettingsAdvanced": IntegerSettingsAdvanced,
    "ChooseUpscaleModel": ChooseUpscaleModel,
    "RegionMaskGenerator": RegionMaskGenerator,
    "RegionMaskValidator": RegionMaskValidator,
    "RegionMaskProcessor": RegionMaskProcessor,
    "RegionMaskConditioning": RegionMaskConditioning,
    "FluxAttentionControl": FluxAttentionControl,
    "RegionOverlayVisualizer": RegionOverlayVisualizer,
    "FluxAttentionCleanup": FluxAttentionCleanup,
    "HiDreamResolutionNode": HiDreamResolutionNode,
    "PerturbationTexture": PerturbationTexture,
    "TextBridge": TextBridge,
    "TwoWaySwitch": TwoWaySwitch,
    "ThreeWaySwitch": ThreeWaySwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "MegapixelCalculatorNode": "ControlAltAI: Megapixel Calculator",
    "FluxSampler": "ControlAltAI: Advanced Sampler",
    "FluxUnionControlNetApply": "ControlAltAI: Union ControlNet Apply",
    "BooleanBasic": "ControlAltAI: Boolean Basic",
    "BooleanReverse": "ControlAltAI: Boolean Reverse",
    "GetImageSizeRatio": "ControlAltAI: Get Image Size Ratio",
    "NoisePlusBlend": "ControlAltAI: Noise Plus Blend",
    "IntegerSettings": "ControlAltAI: Integer Settings",
    "IntegerSettingsAdvanced": "ControlAltAI: Integer Settings Advanced",
    "ChooseUpscaleModel": "ControlAltAI: Choose Upscale Model",
    "RegionMaskGenerator": "ControlAltAI: Region Mask Generator",
    "RegionMaskValidator": "ControlAltAI: Region Mask Validator",
    "RegionMaskProcessor": "ControlAltAI: Region Mask Processor",
    "RegionMaskConditioning": "ControlAltAI: Region Mask Conditioning",
    "FluxAttentionControl": "ControlAltAI: Attention Control",
    "RegionOverlayVisualizer": "ControlAltAI: Region Overlay Visualizer",
    "FluxAttentionCleanup": "ControlAltAI: Attention Cleanup",
    "HiDreamResolutionNode": "ControlAltAI: HiDream Resolution",
    "PerturbationTexture": "ControlAltAI: Perturbation Texture",
    "TextBridge": "ControlAltAI: Text Bridge",
    "TwoWaySwitch": "ControlAltAI: Switch (Two Way)",
    "ThreeWaySwitch": "ControlAltAI: Switch (Three Way)",
}

# Tell ComfyUI where to find JavaScript files
WEB_DIRECTORY = "./web"

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]