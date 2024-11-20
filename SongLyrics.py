def process_lyrics():
    lyrics = [
        "What have I",
        "What have I",
        "What have I done to deserve this"
    ]
    
    word_positions = {}
    for line_number, line in enumerate(lyrics, start=1):
        words = line.strip().split()
        for position, word in enumerate(words, start=1):
            current_position = sum(len(lyrics[i].strip().split()) for i in range(line_number - 1)) + position
            if position == len(words):
                current_position = -current_position
            
            if word in word_positions:
                word_positions[word].append(current_position)
            else:
                word_positions[word] = [current_position]
    
    print("Word Positions Dictionary:")
    for word, positions in word_positions.items():
        print(f"{word}: {positions}")
    
    reconstructed_lyrics = []
    for line_number in range(len(lyrics)):
        words = lyrics[line_number].strip().split()
        reconstructed_line = []
        for word in words:
            positions = word_positions[word]
            reconstructed_line.append(word)
        reconstructed_lyrics.append(" ".join(reconstructed_line))
    
    print("\nReconstructed Lyrics:")
    for line in reconstructed_lyrics:
        print(line)
    
    unique_word_count = len(word_positions)
    print(f"\nTotal Unique Words: {unique_word_count}")
    
    frequency = {word: len(positions) for word, positions in word_positions.items()}
    max_frequency = max(frequency.values())
    most_frequent_words = [word for word, count in frequency.items() if count == max_frequency]
    
    print(f"\nMost Frequent Word(s): {', '.join(most_frequent_words)} (Frequency: {max_frequency})")

process_lyrics()
