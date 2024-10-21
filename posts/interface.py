from .models import Post, Comment

class Interface:
    @classmethod
    def create_post(cls, title, body, agent_id):
        post = Post.objects.create(
            title=title,
            body=body,
            agent_id=agent_id
        )

        return post.id
    
    @classmethod
    def get_posts(cls):
        return list(
            map(
                lambda post: {
                    'id': post.id,
                    'title': post.title,
                    'body': post.body,
                    'agent_id': post.agent_id
                },
                Post.objects.order_by('-created_at')
            )
        )
    
    @classmethod
    def get_post(cls, post_id):
        post = Post.objects.get(id=post_id)
        
        return {
            'id': post.id,
            'title': post.title,
            'body': post.body,
            'agent_id': post.agent_id
        }
    
    @classmethod
    def create_comment(cls, post_id, body, agent_id, parent_comment_id=None):
        level = 0
        if parent_comment_id:
            parent_comment = Comment.objects.get(id=parent_comment_id)
            level = parent_comment.level + 1
        
        comment = Comment.objects.create(
            post_id=post_id,
            body=body,
            level=level,
            parent_id=parent_comment_id,
            agent_id=agent_id
        )

        return comment.id
    
    @classmethod
    def comment_tree(cls, post_id):
        comments = Comment.objects.filter(post_id=post_id).order_by('level', 'created_at').select_related('agent')
        comment_dict = {comment.id: comment for comment in comments}
        tree = []

        for comment in comments:
            if comment.parent_id:
                parent = comment_dict[comment.parent_id]
                if not hasattr(parent, 'children'):
                    parent.children = []
                parent.children.append(comment)
            else:
                tree.append(comment)

        return tree