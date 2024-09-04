use std::{cmp::max, collections::HashSet};

pub struct Solution;

impl Solution {
    /// - Time complexity: O(n)
    /// - Space complexity: O(n)
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
        let dirs: Vec<(i32, i32)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];

        let mut d: usize = 0;

        let mut s: HashSet<(i32, i32)> = HashSet::new();

        for o in obstacles {
            s.insert((o[0], o[1]));
        }

        let mut pos: (i32, i32) = (0, 0);

        let mut ans = 0;

        for com in commands {
            // eprintln!("com={:?}, pos={:?}", com, pos);
            match com {
                -1 => d = (d + 1) % 4,
                -2 => d = (((d as isize - 1) + 4) % 4) as usize,
                _ => {
                    for _ in 0..com {
                        if !s.contains(&(pos.0 + dirs[d].0, pos.1 + dirs[d].1)) {
                            pos.0 += dirs[d].0;
                            pos.1 += dirs[d].1;
                        }
                    }
                }
            }

            ans = max(ans, pos.0 * pos.0 + pos.1 * pos.1);
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::robot_sim(vec![4, -1, 3], vec![]), 25);
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::robot_sim(vec![4, -1, 4, -2, 4], vec![vec![2, 4]]),
            65
        );
    }

    #[test]
    fn test_3() {
        assert_eq!(Solution::robot_sim(vec![6, -1, -1, 6], vec![]), 36);
    }

    #[test]
    fn test_4() {
        assert_eq!(
            Solution::robot_sim(
                vec![-2, 8, 3, 7, -1],
                vec![
                    vec![-4, -1],
                    vec![1, -1],
                    vec![1, 4],
                    vec![5, 0],
                    vec![4, 5],
                    vec![-2, -1],
                    vec![2, -5],
                    vec![5, 1],
                    vec![-3, -1],
                    vec![5, -3]
                ]
            ),
            324
        );
    }
}
