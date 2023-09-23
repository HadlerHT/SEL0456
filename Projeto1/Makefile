# Compiler flags
# -W: Enable all warnings
# -I: Specify additional directories
CFLAGS = -W -Iinclude

# Name of the file directories
SRC_DIR = src
BUILD_DIR = build

# Lists all the .c files in the source directory
SRC_FILES = $(wildcard $(SRC_DIR)/*.c)

# Creates a list of all the .c files in the source directory as .o
OBJ_FILES = $(patsubst $(SRC_DIR)/%.c, $(BUILD_DIR)/%.o, $(SRC_FILES))

# Executable name
TARGET = main

all: $(TARGET)

$(TARGET): $(OBJ_FILES)
	gcc $(CFLAGS) -o $@ $^

$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c | mkdirbuild
	gcc $(CFLAGS) -c $< -o $@

.PHONY: mkdirbuild clean distclean

mkdirbuild:
	@if [ ! -d "$(BUILD_DIR)" ]; then mkdir -p $(BUILD_DIR); fi

clean:
	rm -f -r $(BUILD_DIR)

distclean: clean
	rm -f $(TARGET)



