struct MyCalendar {
    bookings: Vec<(i32, i32)>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendar {
    fn new() -> Self {
        Self {
            bookings: Vec::new(),
        }
    }

    fn book(&mut self, start: i32, end: i32) -> bool {
        let (mut l, mut r) = (-1, self.bookings.len() as isize);

        while r - l > 1 {
            let m = (l + (r - l) / 2);

            if start >= self.bookings[m as usize].0 {
                r = m;
            } else {
                l = m;
            }
        }

        if r != self.bookings.len() as isize && start < self.bookings[r as usize].1 {
            return false;
        }

        if r > 0 && end > self.bookings[(r - 1) as usize].0 {
            return false;
        }
        // println!("start={:?}, end={:?}, r={:?}", start, end, r);

        self.bookings.push((start, end));

        self.bookings.sort();
        self.bookings.reverse();

        true
    }
}
