## 2.1 How does the attention mechanism work
input text -> tokens -> input embedding -> positional encodings to retain the order of tokens

* word embedding captures meaning of each token

* SDPA: Scaled dot product attention : most common way to calculate attention
* aka. self attention

* The scaled attention score is the product of Q and K divided by the square root of the dimension of K, dk

$$\text{Attention}(Q, K, V) = \text{softmax}\!\left(\frac{QK^{T}}{\sqrt{d_k}}\right) V
$$


where,
* $Q$ is shaped $(n, d_k)$ → queries
* $K$ is shaped $(m, d_k)$ → keys
*  K<sup>T</sup> (shaped $(d_k, m)$) is transpose of key matrix

* d<sub>k</sub> is dimension of k e.g. 256

* square root to scale


* output of embedding: 4 tokens × 256 dimensions of embedding vector.
* dimensions of output embedding is preserved by attention.
* This output can be viewed as a contextually enriched combination of the original four tokens.

* multi-head-attention: multiple pairs of queryr, key and values.
* 256-dimensional query, key, and value vectors can be split into say, 8, heads, with 32 dimensional query, key, and value vectors each.
* multiple heads allow it to capture two different meanings of same token. e.g. bank (River Bank, Financial Institute).



## 2.2 How to create a transformer
- pos indicates a token's position in the sequence, while i represents the index within the vector.
- e.g. pos ranges from 0 to len(tokens) and i ranges from 0 to dimenstion_of_embedding_vector

## Code
- adopted from these two repos:
* chinese to english (https://github.com/cuicaihao/Annotated-Transformer-English-to-Chinese-Translator)
* [German To English](https://github.com/harvardnlp/annotated-transformer).
* [books github repo](https://github.com/markhliu/txt2img)
* [colab-notebook](https://colab.research.google.com/drive/1_mKkGGIXbE6efzAmRqpw8MzfYJFtkcFA?usp=sharing)