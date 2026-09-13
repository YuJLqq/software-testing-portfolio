Action()
{

//Correlation comment - Do not change!Original value='143932.199108951HtADfVcptQVzzzzHtttcVpAHtQf' Name ='CorrelationParameter_1'
	web_reg_save_param_ex(
		"ParamName=CorrelationParameter_1",
		"LB=userSession value=",
		"RB=>\n<table border",
		SEARCH_FILTERS,
		"Scope=Body",
		LAST);


	web_url("WebTours",
		"URL=http://127.0.0.1:1080/WebTours",
		"TargetFrame=",
		"Resource=0",
		"RecContentType=text/html",
		"Referer=",
		"Snapshot=t1.inf",
		"Mode=HTML",
		LAST);

	lr_start_transaction("login");

	lr_rendezvous("login");

	web_reg_find("Text=Welcome, <b>{username}",
		LAST);

	lr_think_time(85);

	web_submit_data("login.pl",
		"Action=http://127.0.0.1:1080/WebTours/login.pl",
		"Method=POST",
		"TargetFrame=body",
		"RecContentType=text/html",
		"Referer=http://127.0.0.1:1080/WebTours/nav.pl?in=home",
		"Snapshot=t2.inf",
		"Mode=HTML",
		ITEMDATA,
		"Name=userSession", "Value={CorrelationParameter_1}", ENDITEM,
		"Name=username", "Value={username}", ENDITEM,
		"Name=password", "Value={password}", ENDITEM,
		"Name=JSFormSubmit", "Value=off", ENDITEM,
		"Name=login.x", "Value=52", ENDITEM,
		"Name=login.y", "Value=2", ENDITEM,
		LAST);

	lr_end_transaction("login", LR_AUTO);

return 0;
}

