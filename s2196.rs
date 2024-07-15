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
    /// #BinaryTree
    pub fn create_binary_tree(descriptions: Vec<Vec<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut nodes: std::collections::HashMap<i32, Rc<RefCell<TreeNode>>> =
            std::collections::HashMap::new();
        let mut is_child: std::collections::HashSet<i32> = std::collections::HashSet::new();

        for d in &descriptions {
            nodes.entry(d[0]).or_insert_with(|| {
                let new_node = TreeNode::new(d[0]);
                Rc::new(RefCell::new(new_node))
            });

            is_child.insert(d[1]);

            nodes.entry(d[1]).or_insert_with(|| {
                let new_node = TreeNode::new(d[1]);
                Rc::new(RefCell::new(new_node))
            });

            let parent = nodes.get(&d[0]);
            let child = nodes.get(&d[1]);

            if d[2] == 1 {
                parent.unwrap().borrow_mut().left = Some(child.unwrap().clone());
            } else {
                parent.unwrap().borrow_mut().right = Some(child.unwrap().clone());
            }
        }

        let mut ans: Option<Rc<RefCell<TreeNode>>> = None;
        for d in &descriptions {
            if !is_child.contains(&d[0]) {
                ans = Some(nodes.get(&d[0]).unwrap().clone());
                break;
            }
        }

        ans
    }
}
