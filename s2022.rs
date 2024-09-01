pub struct Solution;

impl Solution {
    /// - Time complexity: O(m * n)
    /// - Space complexity: O(m * n)
    pub fn construct2_d_array(original: Vec<i32>, m: i32, n: i32) -> Vec<Vec<i32>> {
        if original.len() != (n * m) as usize {
            return Vec::<Vec<i32>>::new();
        }
        let mut ans: Vec<Vec<i32>> = vec![vec![0; n as usize]; m as usize];

        for r in 0..m as usize {
            for c in 0..n as usize {
                ans[r][c] = original[r * n as usize + c];
            }
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::construct2_d_array(vec![1, 2, 3, 4], 2, 2),
            [[1, 2], [3, 4]]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::construct2_d_array(vec![1, 2, 3], 1, 3),
            [[1, 2, 3]]
        );
    }

    #[test]

    fn test_3() {
        assert_eq!(
            Solution::construct2_d_array(vec![1, 2], 1, 1),
            Vec::<Vec<i32>>::new()
        );
    }
}
