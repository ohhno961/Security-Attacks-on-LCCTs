#ifndef PROMPT_H
#define PROMPT_H

#include <string>

// Prompt class holds the constructed attack prompt
// Single Responsibility: only stores and provides prompt data
class Prompt {
private:
    std::string content;   // the actual text of the prompt
    std::string filename;  // optional: used in filename-based attacks

public:
    // Constructor: sets the prompt content
    Prompt(std::string content, std::string filename = "")
        : content(content), filename(filename) {}

    // Returns the prompt text
    std::string getContent() const {
        return content;
    }

    // Returns the filename (empty if not used)
    std::string getFilename() const {
        return filename;
    }
};

#endif