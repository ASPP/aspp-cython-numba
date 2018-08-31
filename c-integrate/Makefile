MAKEFLAGS += --no-builtin-rules

CC = gcc
CFLAGS = -g -Wall
LDFLAGS = -lm

LIST = \
     integrate_f8 integrate_f8_3 \
     integrate_f9 integrate_f9_3 \
     integrate_f9_3_native integrate_f9_3_native_fast


timeit: $(LIST)
	for i in $+; \
		do echo $$i; \
		time ./$$i; \
		echo +++++++++++++++++++++++++++++; \
	done

all: $(LIST)

integrate_%: integrate_%.c
	$(CC) $(CFLAGS) $(LDFLAGS) -O0 -o $@ $<

integrate_%_3: integrate_%.c
	$(CC) $(CFLAGS) $(LDFLAGS) -O3 -o $@ $<

integrate_%_3_native: integrate_%.c
	$(CC) $(CFLAGS) $(LDFLAGS) -O3 -march=native -o $@ $<

integrate_%_3_native_fast: integrate_%.c
	$(CC) $(CFLAGS) $(LDFLAGS) -O3 -march=native -ffast-math -o $@ $<
