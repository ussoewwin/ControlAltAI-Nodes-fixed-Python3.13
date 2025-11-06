# ControlAltAI-Nodes-fixed-Python3.13

This is a Python 3.13 compatible version of the original ControlAltAI-Nodes.

## Overview

The original ControlAltAI-Nodes stopped working with Python 3.13, so this version was created with all node names changed. All node names have been modified to avoid conflicts with nodes that have similar names.

## Node Name Changes

All node class names and display names have been changed from the original repository. Here is the complete list of changes:

### Node Class Name and Display Name Changes

| Original Node Class Name | Changed Node Class Name | Original Display Name | Changed Display Name |
|-------------------------|------------------------|----------------------|---------------------|
| FluxResolutionNode | MegapixelCalculatorNode | Flux Resolution Calc | ControlAltAI: Megapixel Calculator |
| FluxSampler | FluxSampler | Flux Sampler | ControlAltAI: Advanced Sampler |
| FluxUnionControlNetApply | FluxUnionControlNetApply | Flux Union ControlNet Apply | ControlAltAI: Union ControlNet Apply |
| BooleanBasic | BooleanBasic | Boolean Basic | ControlAltAI: Boolean Basic |
| BooleanReverse | BooleanReverse | Boolean Reverse | ControlAltAI: Boolean Reverse |
| GetImageSizeRatio | GetImageSizeRatio | Get Image Size Ratio | ControlAltAI: Get Image Size Ratio |
| NoisePlusBlend | NoisePlusBlend | Noise Plus Blend | ControlAltAI: Noise Plus Blend |
| IntegerSettings | IntegerSettings | Integer Settings | ControlAltAI: Integer Settings |
| IntegerSettingsAdvanced | IntegerSettingsAdvanced | Integer Settings Advanced | ControlAltAI: Integer Settings Advanced |
| ChooseUpscaleModel | ChooseUpscaleModel | Choose Upscale Model | ControlAltAI: Choose Upscale Model |
| RegionMaskGenerator | RegionMaskGenerator | Region Mask Generator | ControlAltAI: Region Mask Generator |
| RegionMaskValidator | RegionMaskValidator | Region Mask Validator | ControlAltAI: Region Mask Validator |
| RegionMaskProcessor | RegionMaskProcessor | Region Mask Processor | ControlAltAI: Region Mask Processor |
| RegionMaskConditioning | RegionMaskConditioning | Region Mask Conditioning | ControlAltAI: Region Mask Conditioning |
| FluxAttentionControl | FluxAttentionControl | Flux Attention Control | ControlAltAI: Attention Control |
| RegionOverlayVisualizer | RegionOverlayVisualizer | Region Overlay Visualizer | ControlAltAI: Region Overlay Visualizer |
| FluxAttentionCleanup | FluxAttentionCleanup | Flux Attention Cleanup | ControlAltAI: Attention Cleanup |
| HiDreamResolutionNode | HiDreamResolutionNode | HiDream Resolution | ControlAltAI: HiDream Resolution |
| PerturbationTexture | PerturbationTexture | Perturbation Texture | ControlAltAI: Perturbation Texture |
| TextBridge | TextBridge | Text Bridge | ControlAltAI: Text Bridge |
| TwoWaySwitch | TwoWaySwitch | Switch (Two Way) | ControlAltAI: Switch (Two Way) |
| ThreeWaySwitch | ThreeWaySwitch | Switch (Three Way) | ControlAltAI: Switch (Three Way) |

### Key Changes Summary

1. **FluxResolutionNode → MegapixelCalculatorNode**: The main node class name has been changed, and the file has been renamed from `flux_resolution_cal_node.py` to `megapixel_calculator_node.py`.

2. **All Display Names**: All node display names now have the "ControlAltAI: " prefix to distinguish them from the original nodes.

3. **Display Name Updates**: Some display names have been updated:
   - "Flux Sampler" → "ControlAltAI: Advanced Sampler"
   - "Flux Attention Control" → "ControlAltAI: Attention Control"

## Specifications

For detailed specifications, please refer to the original repository:

**Original Repository**: https://github.com/gseth/ControlAltAI-Nodes

## License

This project is licensed under the MIT License.
