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
    /// 二分探索木のルートを指定すると、同じノード値を持つバランスの取れた二分探索木を返します。
    /// 複数の回答がある場合は、いずれかを返します。
    /// すべてのノードの 2 つのサブツリーの深さが 1 を超えて変わらない場合、二分探索ツリーはバランスが取れています。
    ///
    ///
    /// In-order traversal で、すべての値をソートされたリストに持つ。
    /// その後半分ずつ再帰をしながら BST を構築する。
    ///
    /// - Time complexity: O(n)
    /// - Space compleixty: O(n)
    ///
    /// #BST
    /// #DFS
    pub fn create_sorted_list(root: Option<Rc<RefCell<TreeNode>>>, list: &mut Vec<i32>) {
        if let Some(root) = root {
            let root = root.borrow();

            Self::create_sorted_list(root.left.clone(), list);
            list.push(root.val);
            Self::create_sorted_list(root.right.clone(), list);
        }
    }

    pub fn construct_tree(list: &Vec<i32>, l: isize, r: isize) -> Option<Rc<RefCell<TreeNode>>> {
        if l > r {
            return None;
        }

        let m = l + (r - l) / 2;

        // println!("l={:?}, r={:?}, m={:?}", l, r, m);
        let mut new_tree = TreeNode::new(list[m as usize]);
        new_tree.left = Self::construct_tree(list, l, m - 1);
        new_tree.right = Self::construct_tree(list, m + 1, r);

        Some(Rc::new(RefCell::new(new_tree)))
    }

    pub fn balance_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Option<Rc<RefCell<TreeNode>>> {
        let mut list: Vec<i32> = vec![];

        Self::create_sorted_list(root, &mut list);

        // println!("{:?}", list);
        Self::construct_tree(&list, 0, (list.len() - 1) as isize)
    }
}
