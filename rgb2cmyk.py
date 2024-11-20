def RGB_to_CMYK(rgb):
    r = rgb['R'] / 255.0
    g = rgb['G'] / 255.0
    b = rgb['B'] / 255.0
    
    k = 1 - max(r, g, b)
    
    if k == 1:
        return {'C': 0, 'M': 0, 'Y': 0, 'K': 100}
    
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    
    return {
        'C': round(c * 100),
        'M': round(m * 100),
        'Y': round(y * 100),
        'K': round(k * 100)
    }

def main():
    print("Enter RGB values (R G B) or type 'stop' or 'q' to quit:")
    
    while True:
        user_input = input("Enter RGB values: ")
        
        if user_input.lower() in ['stop', 'q']:
            print("Exiting the program.")
            break
        
        try:
            r, g, b = map(int, user_input.split())
            if any(not (0 <= val <= 255) for val in (r, g, b)):
                print("RGB values must be between 0 and 255.")
                continue
            
            rgb_dict = {'R': r, 'G': g, 'B': b}
            items = rgb_dict.items()
            print(items)

            cmyk = RGB_to_CMYK(rgb_dict)
            print(f"CMYK: {cmyk}")
        
        except ValueError:
            print("Invalid input. Please enter three integers for R, G, and B.")

if __name__ == "__main__":
    main()

