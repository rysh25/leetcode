mod s1381 {
    use std::cmp::min;

    struct CustomStack {
        stack: Vec<i32>,

        curr: i32,
    }

    /**
     * `&self` means the method takes an immutable reference.
     * If you need a mutable reference, change it to `&mut self` instead.
     */
    impl CustomStack {
        fn new(maxSize: i32) -> Self {
            Self {
                stack: vec![-1; maxSize as usize],
                curr: -1,
            }
        }

        fn push(&mut self, x: i32) {
            if self.curr + 1 >= self.stack.len() as i32 {
                return;
            }

            self.curr += 1;

            self.stack[self.curr as usize] = x;
        }

        fn pop(&mut self) -> i32 {
            if self.curr == -1 {
                return -1;
            }

            self.curr -= 1;

            self.stack[self.curr as usize + 1]
        }

        fn increment(&mut self, k: i32, val: i32) {
            for i in 0..min(k as usize, self.stack.len()) {
                self.stack[i] += val;
            }
        }
    }
}
