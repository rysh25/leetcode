pub struct Solution;

impl Solution {
    /// - Time complexity: O(n^2 log n)
    /// - Space complexity: O(n^2)
    pub fn range_sum(nums: Vec<i32>, n: i32, left: i32, right: i32) -> i32 {
        let m: i64 = 1_000_000_007;

        let mut a: Vec<i64> = Vec::new();

        for i in 0..n as usize {
            let mut sum: i64 = 0;
            (i..n as usize).for_each(|j| {
                // println!("i={:?}, j={:?}, nums[j]={:?}, sum={:?}", i, j, nums[j], sum);
                sum += nums[j] as i64 % m;
                a.push(sum);
            });
        }

        a.sort();

        // println!("a={:?}", a);

        (a[left as usize - 1..right as usize].iter().sum::<i64>() % m)
            .try_into()
            .unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::range_sum(vec![1, 2, 3, 4], 4, 1, 5), 13);
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::range_sum(vec![1, 2, 3, 4], 4, 3, 4), 6);
    }

    #[test]

    fn test_3() {
        assert_eq!(Solution::range_sum(vec![1, 2, 3, 4], 4, 1, 10), 50);
    }
}
