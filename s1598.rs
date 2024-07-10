pub struct Solution;

impl Solution {
    /// - Time coplexty: O(n)
    /// - Space complexty: O(1)
    ///
    /// #Stack
    pub fn min_operations(logs: Vec<String>) -> i32 {
        let mut st: Vec<String> = Vec::new();

        for log in logs {
            match log.as_str() {
                "../" => {
                    st.pop();
                }
                "./" => {}
                _ => {
                    st.push(log);
                }
            }
        }

        st.len() as i32
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(
            Solution::min_operations(vec![
                "d1/".to_string(),
                "d2/".to_string(),
                "../".to_string(),
                "d21/".to_string(),
                "./".to_string()
            ]),
            2
        );
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::min_operations(vec![
                "d1/".to_string(),
                "d2/".to_string(),
                "./".to_string(),
                "d3/".to_string(),
                "../".to_string(),
                "d31/".to_string()
            ]),
            3
        );
    }
}
