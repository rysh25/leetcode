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
    pub fn del_nodes(
        root: Option<Rc<RefCell<TreeNode>>>,
        to_delete: Vec<i32>,
    ) -> Vec<Option<Rc<RefCell<TreeNode>>>> {
        let mut ans: Vec<Option<Rc<RefCell<TreeNode>>>> = Vec::new();

        Self::del(root, &to_delete, true, &mut ans);

        ans
    }

    fn del(
        node: Option<Rc<RefCell<TreeNode>>>,
        to_delete: &Vec<i32>,
        add: bool,
        forest: &mut Vec<Option<Rc<RefCell<TreeNode>>>>,
    ) -> bool {
        if node.is_none() {
            return false;
        }

        let binding = node.unwrap();
        let mut node_bollowed = binding.borrow_mut();

        let left = node_bollowed.left.clone();
        let right: Option<Rc<RefCell<TreeNode>>> = node_bollowed.right.clone();

        if to_delete.contains(&node_bollowed.val) {
            if Self::del(left, to_delete, true, forest) {
                node_bollowed.left = None;
            }
            if Self::del(right, to_delete, true, forest) {
                node_bollowed.right = None;
            }

            return true;
        } else {
            if add {
                forest.push(Some(binding.clone()));
            }
            if Self::del(left, to_delete, false, forest) {
                node_bollowed.left = None;
            }
            if Self::del(right, to_delete, false, forest) {
                node_bollowed.right = None;
            }
        }

        false
    }
}
