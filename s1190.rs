pub struct Solution;

impl Solution {
    /// 小文字の英字と括弧で構成される文字列 s が与えられます。
    ///
    /// 一致する括弧の各ペア内の文字列を、最も内側のものから順に反転します。
    /// 結果には括弧を含めないでください。
    ///
    /// - Time complexity: O(n)
    /// - Space complexity: O(n)
    ///
    /// #Stack
    pub fn reverse_parentheses(s: String) -> String {
        let mut st: Vec<String> = vec!["".to_string()];

        for c in s.chars() {
            match c {
                '(' => {
                    st.push("".to_string());
                }
                ')' => {
                    let wk = st.pop().unwrap().chars().rev().collect::<String>();
                    st.last_mut().unwrap().push_str(&wk);
                }
                _ => {
                    st.last_mut().unwrap().push(c);
                }
            }
        }

        st.first().unwrap().to_string()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_1() {
        assert_eq!(Solution::reverse_parentheses("(abcd)".to_string()), "dcba");
    }

    #[test]

    fn test_2() {
        assert_eq!(
            Solution::reverse_parentheses("(u(love)i)".to_string()),
            "iloveu"
        );
    }

    #[test]

    fn test_3() {
        assert_eq!(
            Solution::reverse_parentheses("(ed(et(oc))el)".to_string()),
            "leetcode"
        );
    }
}
