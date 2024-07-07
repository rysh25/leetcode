pub struct Solution;

impl Solution {
    pub fn num_water_bottles(num_bottles: i32, num_exchange: i32) -> i32 {
        let mut ans = 0;

        let mut full = num_bottles;
        let mut empty = 0;

        while full > 0 {
            ans += full;
            empty += full;
            full = empty / num_exchange;
            empty %= num_exchange;
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::num_water_bottles(9, 3), 13);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::num_water_bottles(15, 4), 19);
    }
}
