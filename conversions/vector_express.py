import math
import os, requests
from django.http import request
import json

#https://github.com/smidyo/vectorexpress-api#quickstart
'''GET the a compatible conversion path for your input format and desired output format.
curl https://vector.express/api/v2/public/convert/dxf/auto/svg/

POST to the the first path, with your file as the body
curl --data-binary @myvector.dxf https://vector.express/api/v2/public/convert/dxf/cadlib/svg/

GET the file from the resultUrl
curl https://vector.express/api/v2/public/files/[id].svg --output converted.svg
'''
class File_Conversions:
    def __init__ (self, input_format,output_format,input_file):
        self.input_format = input_format
        self.output_format = output_format
        self.input_file = input_file
        print('self.input_format=',self.input_format)
        print('self.output_format=',self.output_format)
        print('self.input_file=',self.input_file)
        
    def get_conversion_path(self):
        # GET the a compatible conversion path for your input format and desired output format.
        url = 'https://vector.express/api/v2/public/convert/dxf/auto/' + self.input_format + '/'
        response = requests.get(self.url)
        print('response=',response.text)
        return response
    
    '''
    Convert a file
    You can up chain to three programs in the conversion path, and even configure them. See below for all programs and their options.
    POST https://vector.express/api/v2/public/convert/ext/prog1/ext/prog2/ext?prog1-opt=val&prog2-opt=val
    '''
    
    def dxf_dwg_pdf(self):
        '''
        /cad2pdf/  
        Option	                    Type	    Description 
        cad2pdf-auto-fit	        Boolean	    Automatically fit the drawing to to the paper size
        cad2pdf-auto-orientation	Boolean	    Automatically orient the drawing to fit the paper
        cad2pdf-center	            Boolean	    Center the drawing
        cad2pdf-point-size	        Number	    Point size in mm
        cad2pdf-grayscale	        Boolean	    Grayscale
        cad2pdf-landscape	        Boolean	    Use landscape paper
        cad2pdf-margin	            Number	    Margin in millimeter
        cad2pdf-paper-size	        String	    Paper size in the format "WxH"
        cad2pdf-scale	            Number	    Scale the drawing
        cad2pdf-unit	            String	    Override the drawing's unit (in/m/mm)
        '''
        url = 'https://vector.express/api/v2/public/convert/ext/cad2pdf/ext?cad2pdf-opt=val'
        response = requests.get(self.url)
        print('response=',response)
        return response    
    
    def dxf_dwg_svg(self):
        '''
        /cad2svg/  
        Option	                                Type	    Description 
        cad2svg-expand-page-for-stroke-width	Boolean	    Expand the page to accomodate the stroke width
        cad2svg-block	                        String	    Export a specific block
        cad2svg-margin	                        Number	    Margin
        cad2svg-include-bitmaps	                Boolean	    Include bitmaps in the export
        cad2svg-layers	                        String	    Comma delimted list of layers to export
        cad2svg-unit	                        String	    Override the drawing's unit (in/m/mm)
        '''
        url = 'https://vector.express/api/v2/public/convert/ext/cad2pdf/ext?cad2pdf-opt=val'
        response = requests.get(self.url)
        print('response=',response)
        return response    
    
    
    def corel_svg(self):
        '''
        /libcdr/ 
        '''
        url = 'https://vector.express/api/v2/public/convert/ext/libcdr/ext'
        response = requests.get(self.url)
        print('response=',response)
        return response  


    def getfile_plt_svg(self):
        '''
        /uniconvertor/
        '''
        #POST
        headers = {"x-forwarded-proto":"https","x-forwarded-port":"443","host":"postman-echo.com","x-amzn-trace-id":"Root=1-615786cd-12d0b317442e5f7f7b839409","user-agent":"python-requests/2.22.0","accept-encoding":"gzip, deflate","accept":"*/*"}
        url = '--data-binary @PlotFile.plt https://vector.express/api/v2/public/convert/plt/hp2xx/svg/svgo/svg'
        json_data = requests.post(url, headers=headers)
        data = json.loads(json_data)
        id = data["id"]
        print('id=',id)
        #GET
        #url2 = 'https://vector.express/api/v2/public/files/' + id + '.svg --output converted.svg'
        #response = requests.get(url2)
       
        #print('response=',response)
        return json_data 

    def geturl_plt_svg(self):
        '''
        /uniconvertor/
        '''
        #POST
        headers = {"x-forwarded-proto":"https","x-forwarded-port":"443","host":"postman-echo.com","x-amzn-trace-id":"Root=1-615786cd-12d0b317442e5f7f7b839409","user-agent":"python-requests/2.22.0","accept-encoding":"gzip, deflate","accept":"*/*"}
        headers = {"x-forwarded-proto":"https","x-forwarded-port":"443","host":"postman-echo.com","user-agent":"python-requests/2.22.0","accept-encoding":"gzip, deflate","accept":"*/*"}
        
        url = '--data-binary @rQpb9cFyr/PlotFile.plt https://vector.express/api/v2/public/convert/plt/hp2xx/svg/svgo/svg'
        json_data = requests.post(url, headers=headers)
        #data = json.loads(json_data)
        #response = data["resultUrl"]
        print('url=',json_data.text)
        return json_data.reason    
    
    
    def get_converted_file(self):
        url = '--data-binary @PlotFile.plt https://vector.express/api/v2/public/files/[id].' + output_format + ' --output converted.svg'
        response = requests.get(self.url)
        print('response=',response)
        return response 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
