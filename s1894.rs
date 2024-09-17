pub struct Solution;

impl Solution {
    pub fn chalk_replacer(chalk: Vec<i32>, k: i32) -> i32 {
        let sum: i64 = chalk.iter().map(|&x| x as i64).sum();

        let mut rest = (k as i64 + sum) % sum;

        for (i, &c) in chalk.iter().enumerate() {
            if rest < c as i64 {
                return i as i32;
            }

            rest -= c as i64;
        }

        0
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::chalk_replacer(vec![5, 1, 5], 22), 0);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::chalk_replacer(vec![3, 4, 1, 2], 25), 1);
    }
}
