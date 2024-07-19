pub struct Solution;

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;
impl Solution {
    /// - Time complexity: O(n+m)
    /// - Space complexity: O(n+m)
    pub fn count_pairs(root: Option<Rc<RefCell<TreeNode>>>, distance: i32) -> i32 {
        let mut ans = 0;
        Self::dfs(root, distance, &mut ans);

        ans
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, distance: i32, ans: &mut i32) -> Vec<i32> {
        if node.is_none() {
            return vec![0; distance as usize + 1];
        }
        let node = node.unwrap();
        let node_bollowd = node.borrow();
        if node_bollowd.left.is_none() && node_bollowd.right.is_none() {
            let mut res = vec![0; distance as usize + 1];
            res[1] = 1;
            return res;
        }

        let left = Self::dfs(node_bollowd.left.clone(), distance, ans);
        let right = Self::dfs(node_bollowd.right.clone(), distance, ans);

        for l in 1..(distance + 1) {
            for r in (0..distance + 1).rev() {
                if l + r <= distance {
                    *ans += left[l as usize] * right[r as usize];
                }
            }
        }

        let mut res = vec![0; distance as usize + 1];

        for i in 0..(res.len() - 1) {
            res[i + 1] = left[i] + right[i];
        }

        res
    }
}
