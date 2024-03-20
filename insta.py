import instaloader

# extraindo o id do post pelo link


def extract_post_id(link):
    return link.split("/")[-2]


# link do post do insta
post_link = "https://www.instagram.com/p/C4sspsNuq0-/"

# extraindo o id do post
post_id = extract_post_id(post_link)

# criando uma instância do Instaloader
l = instaloader.Instaloader()

# obtendo informações sobre o post
post = instaloader.Post.from_shortcode(L.context, post_id)

# imprimindo algumas informações sobre o post

print("Número de curtidas:", post.likes)
print("Número de comentários:", post.comments)
print("Legenda:", post.caption)
