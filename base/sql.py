# coding: utf-8

SELECT_SESSIONS = u'''
    select s.vg_id,vg.login,inet_ntoa(conv(substr(hex(s.assigned_ip),25,8),16,10)) as ip, s.start_time,s.shape,s.sess_ani 
    from (sessionsradius s, vgroups vg) 
    where s.vg_id = vg.vg_id and vg.login like %s limit 30
'''
SELECT_HIST = u'''
    select a.dt,a.comment,a.ip,a.mac,inet_ntoa(conv(substr(hex(r.rnas),25,8),16,10)) as nas from (auth_history a, rnas r)
    where a.vg_id=%s AND r.nas_id=a.nas_id order by dt desc limit 30
'''
