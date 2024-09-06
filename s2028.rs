pub struct Solution;

impl Solution {
    /// - Time complexity: O(m + n)
    /// - Space complexity: O(n)
    pub fn missing_rolls(rolls: Vec<i32>, mean: i32, n: i32) -> Vec<i32> {
        let m = rolls.len() as i32;

        let sum_all = (n + m) * mean;

        let sum: i32 = rolls.iter().sum();

        // eprintln!(
        //     "sum_all={:?}, sum={:?}, (m + n) * 6={:?}",
        //     sum_all,
        //     sum,
        //     (m + n) * 6
        // );

        let diff = sum_all - sum;

        if diff < n || diff > n * 6 {
            return Vec::new();
        }

        let e = diff / n;
        let r = diff % n;

        let mut ans: Vec<i32> = vec![e; n as usize];
        for i in 0..r {
            ans[i as usize] += 1;
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::missing_rolls(vec![3, 2, 4, 3], 4, 2), [6, 6]);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::missing_rolls(vec![1, 5, 6], 3, 4), [3, 2, 2, 2]);
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::missing_rolls(vec![1, 2, 3, 4], 6, 4), []);
    }
}
