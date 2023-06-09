function Generate-RandomWord {
    $vowels = 'A', 'E', 'I', 'O', 'U'
    $consonants = 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'

    $word = ""
    $length = Get-Random -Minimum 3 -Maximum 9  # Set the length of the word (between 3 and 8 letters)

    for ($i = 0; $i -lt $length; $i++) {
        if ($i % 2 -eq 0) {  # Select a consonant for even positions
            $letter = Get-Random -InputObject $consonants
        }
        else {  # Select a vowel for odd positions
            $letter = Get-Random -InputObject $vowels
        }
        $word += $letter
    }

    return $word
}

$randomWord = Generate-RandomWord
Write-Host "Random Word: $randomWord"
