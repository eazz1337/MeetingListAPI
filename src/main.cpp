 /***************************************************************************
 *                                  _   _ ____  _
 *  Project                     ___| | | |  _ \| |
 *                             / __| | | | |_) | |
 *                            | (__| |_| |  _ <| |___
 *                             \___|\___/|_| \_\_____|
 *
 * Copyright (C) Daniel Stenberg, <daniel@haxx.se>, et al.
 *
 * This software is licensed as described in the file COPYING, which
 * you should have received as part of this distribution. The terms
 * are also available at https://curl.se/docs/copyright.html.
 *
 * You may opt to use, copy, modify, merge, publish, distribute and/or sell
 * copies of the Software, and permit persons to whom the Software is
 * furnished to do so, under the terms of the COPYING file.
 *
 * This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
 * KIND, either express or implied.
 *
 * SPDX-License-Identifier: curl
 *
 ***************************************************************************/
/* <DESC>
 * Very simple HTTP GET
 * </DESC>
 */
#include <stdio.h>
#include <curl/curl.h>
 
int main(void)
{
  CURLcode res;
  FILE *f = fopen("miting_list.csv", "w");
  CURLU *h = curl_url();
  CURL *curl = curl_easy_init();

  if(curl) {
  
    curl_url_set(h, CURLUPART_SCHEME, "https", 0);
    curl_url_set(h, CURLUPART_HOST, "www.bmltadmin.anonimowinarkomani.org", 0);
    curl_url_set(h, CURLUPART_PATH, "/main_server/client_interface/csv/", 0);
    curl_url_set(h, CURLUPART_QUERY, "switcher=GetSearchResults", 0);
    curl_url_set(h, CURLUPART_QUERY,"services=8", CURLU_APPENDQUERY);
    curl_url_set(h, CURLUPART_QUERY, "data_field_key=weekday_tinyint,start_time,duration_time,meeting_name,location_text,location_info,location_street,location_city_subsection,location_municipality", CURLU_APPENDQUERY);

    char *url;
    curl_url_get(h, CURLUPART_URL, &url, 0);
    printf("URL: %s\n", url);

    curl_easy_setopt(curl, CURLOPT_URL, url);
    curl_easy_setopt(curl, CURLOPT_WRITEDATA, f);
 
    /* Perform the request, res gets the return code */
    res = curl_easy_perform(curl);
    /* Check for errors */
    if(res != CURLE_OK)
      fprintf(stderr, "curl_easy_perform() failed: %s\n",
              curl_easy_strerror(res));
 
    /* always cleanup */
    curl_easy_cleanup(curl);
    curl_url_cleanup(h);
    fclose(f);
  }
  return 0;
}