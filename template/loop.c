
int TAG_HEAD_loop_TAG_TAIL(int arg)
{
    arg %= 1000;

    int result = 0;
    for (int i = 0; i < arg; i++) {
        result += RANDOM % 1000;
    }

    while (result > arg) {
        result -= RANDOM % 1000;
    }

    return result;
}

