
# Importação do botcity modo web
from botcity.web import WebBot, Browser, By
# Import for integration with BotCity Maestro SDK
from botcity.maestro import *
# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False
#Importação das opções do navegador
from botcity.web.browsers.chrome import default_options
#atualizar o chromedriver automaticamente
from webdriver_manager.chrome import ChromeDriverManager


class Bot(WebBot):



    def main(self):
        # Runner passes the server url, the id of the task being executed,
        # the access token and the parameters that this task receives (when applicable).
        maestro = BotMaestroSDK.from_sys_args()
        ## Fetch the BotExecution with details from the task, including parameters
        execution = maestro.get_execution()

        print(f"Task ID is: {execution.task_id}")
        print(f"Task Parameters are: {execution.parameters}")

        # modo oculto
        self.headless = False

        #perfil
        profile_path = r'C:\Users\suporteproc\AppData\Local\Google\Chrome\User Data\Profile Selenium'
       
        #opções do navegador
        def_options = default_options(
            headless=self.headless,
            user_data_dir=profile_path  # Inform the profile path that wants to start the browser
        ) 
        self.options = def_options

        #navegador onde está sendo executado
        self.browser = Browser.CHROME

        #chrome drive
        self.driver_path = ChromeDriverManager().install()

        #abrir o site 
        self.browse(self.link)

        # Implement here your logic...
        ...


        self.search_product()


        # Wait 3 seconds before closing
        self.wait(3000)

        # Finish and clean up the Web Browser
        # You MUST invoke the stop_browser to avoid
        # leaving instances of the webdriver open
        self.stop_browser()

        # Uncomment to mark this task as finished on BotMaestro
        # maestro.finish_task(
        #     task_id=execution.task_id,
        #     status=AutomationTaskFinishStatus.SUCCESS,
        #     message="Task Finished OK."
        # )


    def not_found(self, label):
        print(f"Element not found: {label}")


if __name__ == '__main__':
    bot = Bot()
    bot.main()
