import chardet

def detect_encoding(input_string):
    result = chardet.detect(input_string.encode())
    encoding = result['encoding']
    confidence = result['confidence']
    return encoding, confidence

def main():
    input_string = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_hyLicInt}"
    encoding, confidence = detect_encoding(input_string)

    print(f"Detected encoding: {encoding}")
    print(f"Confidence: {confidence:.2f}")

if __name__ == "__main__":
    main()

