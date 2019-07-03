

FROM falconbase AS falcontest

COPY sample_get_json.py sample_get_json.py                                                                                        
COPY sample_get_string.py sample_get_string.py                                                                                    
                                                                                                                                    
ENV PORT 6000                                                                                                                     
EXPOSE 6000                                                                                                                       
                                                                                                                                    
CMD gunicorn --bind 0.0.0.0:6000 sample_get_json:api --reload                                                                     

