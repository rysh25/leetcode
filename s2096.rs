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
    /// - Time complexity: O(n)
    /// - Space complexity: O(n)
    ///
    /// #BinaryTree
    /// #DFS
    pub fn get_directions(
        root: Option<Rc<RefCell<TreeNode>>>,
        start_value: i32,
        dest_value: i32,
    ) -> String {
        let mut start_path: Vec<char> = Vec::new();
        Self::dfs(root.clone(), start_value, &mut start_path);
        start_path.push('S');
        let mut dest_path: Vec<char> = Vec::new();
        Self::dfs(root.clone(), dest_value, &mut dest_path);
        dest_path.push('S');

        // println!("start_path={:?}", start_path);
        // println!("dest_path={:?}", dest_path);

        let mut si = start_path.len() - 1;
        let mut di = dest_path.len() - 1;

        while let (Some(si_new), Some(di_new)) = (si.checked_sub(1), di.checked_sub(1)) {
            if start_path[si_new] != dest_path[di_new] {
                break;
            }
            si = si_new;
            di = di_new;
        }

        // println!("si={:?}, di={:?}", si, di);

        let dest_path: Vec<_> = dest_path.iter().rev().cloned().collect();
        let di = dest_path.len() - di;

        // println!("dest_path={:?}, di={:?}", dest_path, di);

        // println!("start_path slice={:?}", &start_path[..si]);

        let combined_path: Vec<_> = [&vec!['U'; si][..], &dest_path[di..]].concat();
        combined_path.iter().collect()
    }

    fn dfs(node: Option<Rc<RefCell<TreeNode>>>, val: i32, path: &mut Vec<char>) -> bool {
        if node.is_none() {
            return false;
        }

        let binding = node.unwrap();
        let node = binding.borrow();

        if node.val == val {
            return true;
        }

        if Self::dfs(node.left.clone(), val, path) {
            path.push('L');
            return true;
        } else if Self::dfs(node.right.clone(), val, path) {
            path.push('R');
            return true;
        }

        false
    }
}
