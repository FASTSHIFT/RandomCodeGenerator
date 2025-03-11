
int TAG_HEAD_simple_calculation_TAG_TAIL(int arg)
{
    int result = arg;
    result += RANDOM;
    result -= RANDOM;
    result *= RANDOM;
    result /= RANDOM;
    result ^= RANDOM;
    result &= RANDOM;
    result |= RANDOM;
    result %= RANDOM;
    result <<= (RANDOM % 2);
    result >>= (RANDOM % 2);
    return result;
}

