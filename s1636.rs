use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn frequency_sort(nums: Vec<i32>) -> Vec<i32> {
        let mut freq: HashMap<i32, i32> = HashMap::new();

        for &i in &nums {
            *freq.entry(i).or_insert(0) += 1;
        }

        let mut freq_vec: Vec<(_, _)> = nums.iter().map(|&num| (num, freq[&num])).collect();

        // eprintln!("{:?}", freq_vec);

        freq_vec.sort_by(|a, b| {
            let cmp = a.1.cmp(&b.1);
            if cmp == std::cmp::Ordering::Equal {
                b.0.cmp(&a.0)
            } else {
                cmp
            }
        });

        // eprintln!("{:?}", freq_vec);

        freq_vec.into_iter().map(|(key, _)| key).collect()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::frequency_sort(vec![1, 1, 2, 2, 2, 3]),
            [3, 1, 1, 2, 2, 2]
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::frequency_sort(vec![2, 3, 1, 3, 2]),
            [1, 3, 3, 2, 2]
        );
    }
}
