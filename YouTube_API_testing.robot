*** Settings ***
Library           RequestsLibrary
Library           Collections

*** Variables ***
${API_KEY}    
${BASE_URL}    https://www.googleapis.com/youtube/v3

*** Test Cases ***
Najdi videa Hanse Zimmera
    Create Session    youtube    ${BASE_URL}
    ${params}=    Create Dictionary    part=snippet    maxResults=10    q=Hans Zimmer    type=video    key=${API_KEY}
    ${response}=    Get Request    youtube    /search    params=${params}
    Should Be Equal As Strings    ${response.status_code}    200
    ${video_ids}=    Evaluate    [item['id']['videoId'] for item in $response.json()['items']]    json
    ${video_detaily}=    Get Video Details    ${video_ids}
    ${delka_time}=    Get Duration Of Specific Track    ${video_detaily}    Time
    Log    Duration of 'Time' by Hans Zimmer: ${delka_time}

*** Keywords ***
Podrobnosti videí
    [Arguments]    ${video_ids}
    ${video_detaily}=    Create List
    FOR    ${id}    IN    @{video_ids}
        ${params}=    Create Dictionary    part=contentDetails    id=${id}    key=${API_KEY}
        ${response}=    Get Request    youtube    /videos    params=${params}
        Append To List    ${video_detaily}    ${response.json()}
    END
    [Return]    ${video_detaily}

Získej délku skladby Time
    [Arguments]    ${video_detaily}    ${track_name}
    FOR    ${detail}    IN    @{video_detaily}
        ${title}=    Set Variable    ${detail['items'][0]['snippet']['title']}
        Continue For Loop If    not ('${track_name}' in '${title}')
        ${delka}=    Set Variable    ${detail['items'][0]['contentDetails']['delka']}
        [Return]    ${delka}
    END
    [Return]    None
