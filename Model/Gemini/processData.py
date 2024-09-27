def processData(text):
    # Separates slides
    slides = text.split('---SLIDE ')
    
    material = []
    image = []
    
    # Loop each slide in slides
    for slide in slides:
        # Remove empty index
        slide = slide.strip()
        if slide:
            # Separate each slide into material part and image part
            parts = slide.split('Image description for slide:')
            material.append(parts[0].strip())
            image.append(parts[1].strip() if len(parts) > 1 else '')

    return material, image