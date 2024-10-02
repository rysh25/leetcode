use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let n = arr.len();
        let mut copy = arr.clone();
        copy.sort();

        let mut rank: HashMap<i32, i32> = HashMap::new();

        let mut prev = -1;
        let mut r = 0;

        for a in &copy {
            if prev != *a {
                r += 1;
                rank.insert(*a, r);
            }

            prev = *a;
        }

        let mut ans = vec![0; n];

        for (i, a) in arr.iter().enumerate() {
            ans[i] = *rank.get(a).unwrap();
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
            Solution::array_rank_transform(vec![40, 10, 20, 30]),
            [4, 1, 2, 3],
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::array_rank_transform(vec![100, 100, 100]),
            [1, 1, 1],
        );
    }

    #[test]

    fn test_3() {
        assert_eq!(
            Solution::array_rank_transform(vec![37, 12, 28, 9, 100, 56, 80, 5, 12]),
            [5, 3, 4, 2, 8, 6, 7, 1, 3],
        );
    }
}
