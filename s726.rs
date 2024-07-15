pub struct Solution;

impl Solution {
    pub fn count_of_atoms(formula: String) -> String {
        let mut st: Vec<std::collections::BTreeMap<String, usize>> = Vec::new();

        st.push(std::collections::BTreeMap::new());

        let (mut atom, mut digits) = (String::new(), String::new());
        let n = formula.len();
        let chars: Vec<char> = formula.chars().collect();
        let mut i = 0;
        while i < n {
            let c = chars[i];

            if c == '(' {
                st.push(std::collections::BTreeMap::new());
            } else if c == ')' {
                digits.clear();
                let mut j = i + 1;
                if j < n {
                    while j < n && chars[j].is_numeric() {
                        digits.push_str(&chars[j].to_string());
                        j += 1
                    }
                }

                i = j - 1;

                if !digits.is_empty() {
                    let v: usize = digits.parse().unwrap();
                    let map = st.last_mut().unwrap();
                    let entries: Vec<(&String, &mut usize)> = map.iter_mut().collect();
                    for (_, value) in entries {
                        *value *= v;
                    }
                };

                if let Some(mut last_map) = st.pop() {
                    if let Some(current_last_map) = st.last_mut() {
                        for (key, value) in last_map.into_iter() {
                            *current_last_map.entry(key).or_insert(0) += value;
                        }
                    } else {
                        st.push(last_map);
                    }
                }
            } else if c.is_uppercase() {
                atom.clear();
                atom.push_str(&c.to_string());

                let mut j = i + 1;
                if j < n {
                    while j < n && chars[j].is_lowercase() {
                        atom.push_str(&chars[j].to_string());
                        j += 1;
                    }
                }

                i = j - 1;

                digits.clear();
                let mut j = i + 1;
                if j < n {
                    while j < n && chars[j].is_numeric() {
                        digits.push_str(&chars[j].to_string());
                        j += 1
                    }
                }

                i = j - 1;

                let v = if digits.is_empty() {
                    1
                } else {
                    digits.parse().unwrap()
                };

                *st.last_mut().unwrap().entry(atom.clone()).or_insert(0) += v;
            }

            i += 1;
        }
        let last: std::collections::BTreeMap<String, usize> = st.pop().unwrap();
        let mut ans = String::new();

        for (key, value) in last {
            if value == 1 {
                ans.push_str(&key);
            } else {
                ans.push_str(&format!("{}{}", key, value));
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
        assert_eq!(Solution::count_of_atoms("H2O".to_string()), "H2O");
    }

    #[test]

    fn test_2() {
        assert_eq!(Solution::count_of_atoms("Mg(OH)2".to_string()), "H2MgO2");
    }

    #[test]

    fn test_3() {
        assert_eq!(
            Solution::count_of_atoms("K4(ON(SO3)2)2".to_string()),
            "K4N2O14S4"
        );
    }
}
