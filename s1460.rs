pub struct Solution;

impl Solution {
    /// - Time complexity: O(n log n)
    /// - Space complexity: O(1)
    ///
    /// #Sorting
    pub fn can_be_equal(mut target: Vec<i32>, mut arr: Vec<i32>) -> bool {
        target.sort();

        arr.sort();

        if target == arr {
            return true;
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert!(Solution::can_be_equal(vec![1, 2, 3, 4], vec![2, 4, 1, 3]));
    }

    #[test]

    fn test_2() {
        assert!(Solution::can_be_equal(vec![7], vec![7]));
    }
}
