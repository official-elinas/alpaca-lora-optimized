import transformers

from utils.monkeypatches.flash_attn_llama import llama_flash_attention_forward, _prepare_decoder_attention_mask
from utils.monkeypatches.sdp_llama import sdp_attention_forward
from utils.monkeypatches.xformers_llama import llama_attention_forward
from utils.monkeypatches.xpos_rope_llama_monkey_patch import XposRotaryEmbedding, apply_rotary_pos_emb


# from monkeypatches.xformers_gpt import (gpt2_wrapped_scaled_dot_product, gpt_merge_heads)


def apply_xformers_monkeypatches() -> None:
    # LLaMA
    transformers.models.llama.modeling_llama.LlamaAttention.forward = llama_attention_forward
    # GPT-J
    # transformers.models.gptj.modeling_gptj.GPTJAttention._attn = gpt2_wrapped_scaled_dot_product
    # transformers.models.gptj.modeling_gptj.GPTJAttention._merge_heads = gpt_merge_heads
    #
    # # NeoX
    # transformers.models.gpt_neox.modeling_gpt_neox.GPTNeoXAttention._attn = gpt2_wrapped_scaled_dot_product
    # transformers.models.gpt_neox.modeling_gpt_neox.GPTNeoXAttention._merge_heads = gpt_merge_heads


def apply_sdp_attention_monkeypatch() -> None:
    transformers.models.llama.modeling_llama.LlamaAttention.forward = sdp_attention_forward


def apply_flash_attention_monkeypatch() -> None:
    transformers.models.llama.modeling_llama.LlamaModel._prepare_decoder_attention_mask = (
        _prepare_decoder_attention_mask
    )
    transformers.models.llama.modeling_llama.LlamaAttention.forward = llama_flash_attention_forward


def apply_rope_monkeypatch() -> None:
    transformers.models.llama.modeling_llama.LlamaRotaryEmbedding = XposRotaryEmbedding
    transformers.models.llama.modeling_llama.apply_rotary_pos_emb = apply_rotary_pos_emb


