int first_func(int a, char b) {
  if (a >= 0) return a + 3;
  return a - 1;
}

int global_var = 3;

int main() {
  int res = 0;
  for (int i = 0; i < 3; i++) {
    res += first_func(i, 'a');
  }
  return res;
}
