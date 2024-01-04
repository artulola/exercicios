from datetime import datetime, timezone, timedelta

currentUserId = 0
currentPostId = 0

class AuthenticatableMixin:
    def authenticate(self, user, enteredLogin, enteredPassword):
        if user.getLogin() == enteredLogin and user.getPassword() == enteredPassword:
            return True
        else:
            return False

class User(AuthenticatableMixin):
    def __init__(self, name, login, password):
        global currentUserId
        self.__id = currentUserId
        currentUserId += 1
        self.__name = name
        self.__login = login
        self.__password = password

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getLogin(self):
        return self.__login

    def getPassword(self):
        return self.__password

    def __str__(self):
        return self.__name

class Post:
    def __init__(self, title, text, publicationDate, user):
        global currentPostId
        self.__id = currentPostId
        currentPostId += 1
        self.__title = title
        self.__text = text
        self.__publicationDate = publicationDate
        self.__user = user

    def getId(self):
        return self.__id

    def getTitle(self):
        return self.__title

    def getText(self):
        return self.__text

    def getPublicationDate(self):
        return self.__publicationDate

    def setPublicationDate(self, publicationDate):
        self.__publicationDate = publicationDate

    def getUser(self):
        return self.__user

    def __str__(self):
        return f"ID: {self.__id}\nTítulo: {self.__title}\nUsuário: {self.__user}\nData de publicação: {self.__publicationDate}"

class Blog:
    def __init__(self):
        self.__posts = []

    def addPost(self, post):
        self.__posts.append(post)

    def publishPost(self, post):
        data = datetime.today().astimezone(timezone(timedelta(hours=-3))).strftime('%d/%m/%Y %H:%M')
        dataPub = datetime.strptime(data, '%d/%m/%Y %H:%M')
        post.setPublicationDate(dataPub)

    def listPublishedPosts(self):
        currentDate = datetime.today().astimezone(timezone(timedelta(hours=-3))).strftime('%d/%m/%Y %H:%M')
        publishedPostsList = []
        for post in self.__posts:
            if post.getPublicationDate().strftime('%d/%m/%Y %H:%M') <= currentDate:
                publishedPostsList.append(post)
        return publishedPostsList

    def listAllPosts(self):
        return self.__posts

    def deletePost(self, post):
        self.__posts.remove(post)

class BlogSystem:
    def __init__(self):
        self.blog = Blog()
        self.users = []
        self.authenticatedUser = None
        self.active = True
        self.activeBlog = False
        self.userOptions = {
            "1": self.registerUser,
            "2": self.login,
            "0": self.end
        }
        self.blogOptions = {
            "1": self.addPost,
            "2": self.publishPost,
            "3": self.listPublishedPosts,
            "4": self.listAllPosts,
            "5": self.deletePost,
            "0": self.exit
        }

    def showUserMenu(self):
        print("ÁREA DO USUÁRIO")
        print("-----")
        print("1. Registrar Usuário")
        print("2. Login")
        print("0. Sair")

    def showBlogMenu(self):
        print("BLOG")
        print("-----")
        print("1. Adicionar post")
        print("2. Publicar post")
        print("3. Listar posts publicados")
        print("4. Listar todos os posts")
        print("5. Apagar post")
        print("0. Sair")

    def execute(self):
        while self.active:
            self.showUserMenu()
            op = input("Digite uma opção: ")
            action = self.userOptions.get(op)
            if action:
                action()
                if self.activeBlog:
                    self.__executeBlog()
            else:
                print("\nOpção inválida.\n")

    def __executeBlog(self):
        while self.activeBlog:
            self.showBlogMenu()
            op = input("Digite uma opção: ")
            action = self.blogOptions.get(op)
            if action:
                action()
            else:
                print("\nOpção inválida.\n")

    def registerUser(self):
        print("\nRegistrar Usuário")
        name = input("Nome: ")
        login = input("Login: ")
        password = input("Senha: ")
        user = User(name, login, password)
        self.users.append(user)
        print("Usuário registrado.\n")

    def login(self):
        print("\nLogin")
        login = input("Login: ")
        password = input("Senha: ")
        if not self.users:
            print("Nenhum usuário registrado no sistema.\n")
        else:
            for user in self.users:
                if user.authenticate(user, login, password):
                    print("Usuário autenticado.\n")
                    self.activeBlog = True
                    self.authenticatedUser = user
                    break
                elif user == self.users[-1]:
                    print("Login e/ou senha inválidos.\n")

    def end(self):
        self.active = False
        print("\nPrograma fechado.")

    def addPost(self):
        print("\nAdicionar post")
        title = input("Título: ")
        text = input("Texto: ")
        dateInput = input("Data de publicação: ")
        publicationDate = datetime.strptime(dateInput, '%d/%m/%Y %H:%M')
        post = Post(title, text, publicationDate, self.authenticatedUser)
        self.blog.addPost(post)
        print("Post adicionado.\n")

    def publishPost(self):
        print("\nPublicar post")
        posts = self.blog.listAllPosts()
        postId = int(input("ID do post: "))
        if not posts:
            print("Nenhum post encontrado.\n")
        else:
            for post in posts:
                if postId == post.getId():
                    self.blog.publishPost(post)
                    print("Post publicado.\n")
                elif post == posts[-1]:
                    print("Esse post não existe.\n")

    def listPublishedPosts(self):
        print("\nPosts publicados:")
        list = self.blog.listPublishedPosts()
        if not list:
            print("Nenhum post publicado.\n")
        else:
            for post in list:
                print("-----")
                print(post)
            print("")

    def listAllPosts(self):
        print("\nPosts:")
        list = self.blog.listAllPosts()
        if not list:
            print("Nenhum post no blog.\n")
        else:
            for post in list:
                print("-----")
                print(post)
            print("")

    def deletePost(self):
        print("\nApagar post")
        posts = self.blog.listAllPosts()
        postId = int(input("ID post: "))
        if not posts:
            print("Nenhum post no blog.\n")
        else:
            for post in posts:
                if postId == post.getId():
                    self.blog.deletePost(post)
                    print("Post apagado.\n")
                elif post == posts[-1]:
                    print("O post não existe.\n")

    def exit(self):
        self.activeBlog = False
        print("Saindo...\n")

if __name__ == '__main__':
    BlogSystem().execute()
