

int TAG_HEAD_recursive_calls_TAG_TAIL(int arg)
{
    if (arg < 0) {
        return 0;
    }

    arg %= (RANDOM % 64);

    if (TAG_HEAD_recursive_calls_TAG_TAIL(arg - 1) == 0) {
        return 0;
    }

    return arg;
}