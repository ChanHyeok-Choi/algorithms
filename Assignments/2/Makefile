# Writer: 20181257 ChanHyeok Choi\
  This is Makefile for that sum_dist.o and clean method for building and clearing all file made from "make".

CC = g++
TARGET = sum_dist
OBJS = sum_dist.o
CXXFLAGS += -Wall -std=c++17 -g -pedantic

all : $(TARGET)

$(TARGET) : $(OBJS)
	$(CC) -o $@ $^

.c.o:
	$(CC) $(CXXFLAGS) -c -o $@ $<

.phony: clean
clean:
	rm -f $(TARGET) $(OBJS)