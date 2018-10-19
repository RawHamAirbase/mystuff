text = "X-DSPAM-Confidence:    0.8475"
beg = text.find(str(0))
print(float(text[beg:]))
