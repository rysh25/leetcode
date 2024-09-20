pub struct Solution;

impl Solution {
    pub fn diff_ways_to_compute(expression: String) -> Vec<i32> {
        let mut ans = Vec::new();

        for (i, oper) in expression.chars().enumerate() {
            if oper == '+' || oper == '-' || oper == '*' {
                let s1 = Solution::diff_ways_to_compute(expression[0..i].to_string());
                let s2 = Solution::diff_ways_to_compute(expression[i + 1..].to_string());
                for &a in &s1 {
                    for &b in &s2 {
                        match oper {
                            '+' => ans.push(a + b),
                            '-' => ans.push(a - b),
                            '*' => ans.push(a * b),
                            _ => (),
                        }
                    }
                }
            }
        }

        if ans.is_empty() {
            ans.push(expression.parse().unwrap());
        }

        ans
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::diff_ways_to_compute("2-1-1".to_string()), [0, 2]);
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::diff_ways_to_compute("2*3-4*5".to_string()),
            [-34, -14, -10, -10, 10]
        );
    }
}
