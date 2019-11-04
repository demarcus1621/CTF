"""
URL Parser
"""

import sys

# GLOBAL VARIABLES
URL = None
SCHEME = None
HIERARCHICAL_URL_IDENTIFIER = None
USERNAME = None
PASSWORD = None
AUTHORITY_SECTION = None
DESTINATION_ADDRESS = None
SERVER_PATH = None
QUERY_STRING = None
FRAGMENT_NAME = None
FIRST_OCCURANCE = None
LOCATION_LIST = None

def main():
    global URL
    global SCHEME
    global HIERARCHICAL_URL_IDENTIFIER
    global USERNAME
    global PASSWORD
    global DESTINATION_ADDRESS
    global SERVER_PATH
    global QUERY_STRING
    global FRAGMENT_NAME
    global FIRST_OCCURANCE
    global AUTHORITY_SECTION
    global LOCATION_LIST
    
    URL = sys.argv[1:]
    for url in URL:
        #Extract scheme
        SCHEME, leftover = url[:url.find(":")], url[url.find(":")+1:]
        SCHEME += ":"
        
        #Test for hierarchical URL identifier
        if leftover[:2] != "//":
            HIERARCHICAL_URL_IDENTIFIER = False
        else:
            HIERARCHICAL_URL_IDENTIFIER = True
        
        if HIERARCHICAL_URL_IDENTIFIER:
            #Remove // from URL
            leftover = leftover[2:]
            
            #Pull Authority Section
            if "/" or "\\" or "?" or "#" in leftover:
                find_forward_slash = leftover.find("/")
                find_back_slash = leftover.find("\\")
                find_question_mark = leftover.find("?")
                find_fragment_mark = leftover.find("#")
                LOCATION_LIST = [find_back_slash, find_forward_slash, find_question_mark, find_fragment_mark]
                for symbol in LOCATION_LIST:
                    if symbol < 0:
                        LOCATION_LIST.remove(symbol)
                FIRST_OCCURANCE = min(LOCATION_LIST)
                AUTHORITY_SECTION = leftover[:FIRST_OCCURANCE]
            else:
                AUTHORITY_SECTION = leftover
            
            #Parse Authority Section
            #DESTINATION_ADDRESS includes PORT value separated by :
            if "@" in AUTHORITY_SECTION:
                if ":" in AUTHORITY_SECTION.split("@")[0]:
                    USERNAME = AUTHORITY_SECTION[:AUTHORITY_SECTION.find(":")]
                    PASSWORD = AUTHORITY_SECTION[AUTHORITY_SECTION.find(":"):AUTHORITY_SECTION.find("@")]
                    DESTINATION_ADDRESS = AUTHORITY_SECTION[AUTHORITY_SECTION.find("@"):]
                else:
                    USERNAME = AUTHORITY_SECTION[:AUTHORITY_SECTION.find("@")]
                    DESTINATION_ADDRESS = AUTHORITY_SECTION[AUTHORITY_SECTION.find("@"):]
            else:
                DESTINATION_ADDRESS = AUTHORITY_SECTION
            
            #Find server path
            if FIRST_OCCURANCE:
                if find_forward_slash < 0 and find_back_slash > 0:
                    print("back slash found")
                elif find_forward_slash > 0 and find_back_slash < 0:
                    print("forward slash found")
                else:
                    print("no slash found")
        else:
            print("Non-hierarchical URL, passing")
            continue
    
if __name__ == "__main__":
    main()